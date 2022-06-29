import numpy as np
import matplotlib.pyplot as plt

# Generador basado en ejemplo del curso CS231 de Stanford: 
# CS231n Convolutional Neural Networks for Visual Recognition
# (https://cs231n.github.io/neural-networks-case-study/)

def cardinal_sine_data_generator(x1_neg_lim,x1_pos_lim,x2_neg_lim,x2_pos_lim,number_of_examples,plot_data):
    """Receives x1 and x2 limits and generates a number of examples based in a sine cardinal function with noise 
    It plots the data if plot_data is True.

    Args:
        axis_lims (_float_): Limits of the working function
        number_of_examples (_int_): Number of examples to generate
        plot_data (_bool_): If True, plots the data
    
    Returns:
        x (_np array->3n x 2_): 2 Features
        y (_np array->3n x 1_): Function values

    """
    #Generate arrays of x1 and x2 that go from -14 to +14 with a step of 0.1
    x1_axis_values = np.arange(x1_neg_lim,x1_pos_lim,0.1)
    x2_axis_values = np.arange(x2_neg_lim,x2_pos_lim,0.1)

    x1_matrix = np.tile(x1_axis_values,(len(x2_axis_values),1))
    x1_matrix=x1_matrix.T
    #Create a matrix x2 with x2 as rows repeated according to size of x1
    x2_matrix = np.tile(x2_axis_values,(len(x1_axis_values),1))

    #Cardinal sine based function, with particular modifications
    y_matrix=-10*np.sin(np.sqrt(x1_matrix**2+x2_matrix**2))/np.sqrt(x1_matrix**2+x2_matrix**2)+50
    
    #Create a matrix of random gaussian numbers with the size of y and values between -1 and 1
    noise = np.random.normal(0,0.5,y_matrix.shape)
    y_matrix+=noise
    if plot_data:
        #Make a 3D plot of y_matrix 
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.plot_surface(x1_matrix,x2_matrix,y_matrix,cmap='viridis',edgecolor='none')
        ax.set_xlabel('x1')
        ax.set_ylabel('x2')
        ax.set_zlabel('y')
        ax.set_title('Original training function')
        plt.show()


    #Generate random examples based on the previous function
    #Generate number_of_examples random floats between x1_neg_lim and x1_pos_lim
    x1= np.random.uniform(x1_neg_lim,x1_pos_lim,number_of_examples)
    x2= np.random.uniform(x2_neg_lim,x2_pos_lim,number_of_examples)
    
    x= np.column_stack((x1,x2))
    y= -10*np.sin(np.sqrt(x1**2+x2**2))/np.sqrt(x1**2+x2**2)+50+np.random.normal(0,0.5,number_of_examples)
    
    if plot_data:
        #Plot the random generation of examples
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        #Plot the 3D plot of the points with x as axis and y as its value
        ax.scatter(x[:,0],x[:,1],y,c='r',marker='o')
        ax.set_xlabel('x1')
        ax.set_ylabel('x2')
        ax.set_zlabel('y')
        ax.set_title('Random generation of examples')
        plt.show()

    y=y.reshape(number_of_examples,1)
    return x,y

def sigmoid(x):
    """Sigmoid function.
    Args:
        x (np array): Input data
    Returns:
        np array: Output data
    """
    return 1 / (1 + np.exp(-x))

def random_extract(x,t,extract_size):
    """Extracts a random subset of the data.
    Args:
        x (np array): Input data (Features)
        t (np array): Targets
        extract_size (int): Size of the subset to extract
    Returns:
        np array: Input data (Features)
        np array: Targets
    """
    rand_indices = np.random.choice(x.shape[0], extract_size, replace=False)
    x_rand=x[rand_indices]
    t_rand=t[rand_indices]
    x_red=np.delete(x, rand_indices, axis=0)
    t_red=np.delete(t, rand_indices, axis=0)

    return x_red,t_red,x_rand,t_rand

def normalization(x):
    """Normalizes the input data between 1 and -1.

    Args:
        x (np array): Input data

    Returns:
        np array: Normalized input data
    """
    mu=np.mean(x)
    x_norm=(x - mu) / np.max(np.abs(x))
    return x_norm,mu
    #As we know that features are between -14 and 14 we can use max without risk of picking one outlier.
    #In a real application we should kick outliers

def inicializar_pesos(n_entrada, n_capa_2, n_capa_3):
    """Randomly initializes the weights and biases of the neural network.
    Args:
        n_entrada (int): Neurons in the input layer
        n_capa_2 (int): Neurons in the hidden layer
        n_capa_3 (int): Neurons in the output layer
    Returns:
        dictionary: It contains the weights and biases of the neural network.
    """
    randomgen = np.random.default_rng()

    w1 = 0.01 * randomgen.standard_normal((n_entrada, n_capa_2))
    b1 = 0.01 * randomgen.standard_normal((1, n_capa_2))

    w2 = 0.01 * randomgen.standard_normal((n_capa_2, n_capa_3))
    b2 = 0.01 * randomgen.standard_normal((1,n_capa_3))

    return {"w1": w1, "b1": b1, "w2": w2, "b2": b2}

def ejecutar_adelante(x, pesos):
    """Runs Forward Propagation on the neural network.

    Args:
        x (np array): Input data (Features)
        pesos (dictionary): Weights and biases of the neural network

    Returns:
        dictionary: Contains the output and intermidiate varaibles of the neural network.
    """

    # Funcion de entrada (a.k.a. "regla de propagacion") para la primera capa oculta
    z = x.dot(pesos["w1"]) + pesos["b1"]

    # Funcion de activacion Sigmoid
    h = sigmoid(z)

    # Salida de la red (funcion de activacion lineal). Esto incluye la salida de todas
    # las neuronas y para todos los ejemplos proporcionados
    y = h.dot(pesos["w2"]) + pesos["b2"]

    return {"z": z, "h": h, "y": y}


def Loss(y, t):
    
    """Calculates the MSE loss of the neural network.

    Args:
        y (np array): Output of the neural network
        t (np array): Targets

    Returns:
        int: Total loss of the neural network
    """
    return np.mean((t - y) ** 2)


def back_propagation(x,t,h,z,w2,y):

    """Calculates changes for weights and biases of the neural network.

    Args:
        x (np array): Input data (Features)
        t (np array): Targets
        h (np array): Output of the hidden layer
        z (np array): Input of the hidden layer
        w2(np array): Weights of the output layer
        y (np array): Output of the output layer

    Returns:
        dL_dw1 (np array): Change in the weights of the input layer
        dL_db1 (np array): Change in the biases of the input layer
        dL_dw2 (np array): Change in the weights of the output layer
        dL_db2 (np array): Change in the biases of the output layer
        
    """
    m=np.size(x, 0)

    dL_dy = 2*(y-t)/m        #(changed)

    dL_dw2 = h.T.dot(dL_dy)                         # Ajuste para w2    (= to classification)
    dL_db2 = np.sum(dL_dy, axis=0, keepdims=True)   # Ajuste para b2    (= to classification)

    dL_dh = dL_dy.dot(w2.T)     #(= to classification)
    

    dh_dz=sigmoid(z)*(1-sigmoid(z)) #(changed)
    dL_dz = dL_dh*dh_dz             #(changed)

    dL_dw1 = x.T.dot(dL_dz)                         # Ajuste para w1
    dL_db1 = np.sum(dL_dz, axis=0, keepdims=True)   # Ajuste para b1
    return dL_dw1, dL_db1, dL_dw2, dL_db2


# x: n entradas para cada uno de los m ejemplos(nxm)
# t: salida correcta (target) para cada uno de los m ejemplos (m x 1)
# pesos: pesos (W y b)
# La función actualiza el valor del diccionario pesos
def train(x, t, pesos, learning_rate, epochs):
    """Changes the weights and biases(all in the dictionary "pesos") of the neural network. 

    Args:
        x (np array): Input data (Features)
        t (np array): Output data (Targets)
        pesos (dictionary): Weights and biases of the neural network
        learning_rate (float): Hyperparameter that determines the pace of change of the weights for each epoch
        epochs (int): Number of epochs to train the neural network
    """

    for i in range(epochs):
        # Ejecucion de la red hacia adelante
        resultados_feed_forward = ejecutar_adelante(x, pesos)
        y = resultados_feed_forward["y"]
        h = resultados_feed_forward["h"]
        z = resultados_feed_forward["z"]

        # LOSS
        loss = Loss(y, t)

        if iteration == N:
            iteration = 0

            resultados_feed_forward_validation = ejecutar_adelante(x_val, pesos)
            y_val = resultados_feed_forward_validation["y"]
            # exp_scores_validation = np.exp(y_val)
            # sum_exp_scores_validation = np.sum(exp_scores_validation, axis=1, keepdims=True)
            # p_val = exp_scores_validation / sum_exp_scores_validation

            #validation_loss = (1 / m_val) * np.sum( -np.log( p_val[range(m_val), t_val] ))

            _, validation_loss = Loss(y_val, t_val)
            if internal_counter == 0:
                pass
            else:
                if validation_loss > (validation_loss_ant):
                    print("Overfitting")
                    verify = True
            internal_counter = internal_counter + 1
            validation_loss_ant = validation_loss

        if verify:
            break
        iteration = iteration + 1

        # Mostramos solo cada 100 epochs
        if i %1 == 0:
            print("Loss epoch", i, ":", loss)

        # Extraemos los pesos a variables locales
        w1 = pesos["w1"]
        b1 = pesos["b1"]
        w2 = pesos["w2"]
        b2 = pesos["b2"]

        # Ajustamos los pesos: Backpropagation
        dL_dw1, dL_db1, dL_dw2, dL_db2=back_propagation(x,t,h,z,w2,y)


        # Aplicamos el ajuste a los pesos
        w1 += -learning_rate * dL_dw1
        b1 += -learning_rate * dL_db1
        w2 += -learning_rate * dL_dw2
        b2 += -learning_rate * dL_db2

        # Actualizamos la estructura de pesos
        # Extraemos los pesos a variables locales
        pesos["w1"] = w1
        pesos["b1"] = b1
        pesos["w2"] = w2
        pesos["b2"] = b2


def iniciar(numero_ejemplos, graficar_datos):
    """Runs all the NN functions.

    Args:
        numero_clases (int): Number of classes
        numero_ejemplos (int): Number of examples
        graficar_datos (bool): If True, plots the data
    """

    # Generamos datos
    x_train, t_train = cardinal_sine_data_generator(-14,14,-14,14,numero_ejemplos,graficar_datos)
    x_train[:,0],x0_mu=normalization(x_train[:,0])
    x_train[:,1],x1_mu=normalization(x_train[:,1])
    # Split the data
    x_train,t_train,x_val,t_val=random_extract(x_train,t_train,int(numero_ejemplos/5))
    x_train,t_train,x_test,t_test=random_extract(x_train,t_train,int(numero_ejemplos/5))
    
   

    # Inicializa pesos de la red
    NEURONAS_CAPA_OCULTA = 100
    NEURONAS_ENTRADA = 2
    pesos = inicializar_pesos(n_entrada=NEURONAS_ENTRADA, n_capa_2=NEURONAS_CAPA_OCULTA, n_capa_3=1)

    # Entrena
    LEARNING_RATE=0.01
    EPOCHS=101
    train(x_train, t_train, pesos, LEARNING_RATE, EPOCHS)



iniciar(numero_ejemplos=1000, graficar_datos=True)