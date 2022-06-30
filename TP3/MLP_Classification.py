import numpy as np
import matplotlib.pyplot as plt

# Generador basado en ejemplo del curso CS231 de Stanford: 
# CS231n Convolutional Neural Networks for Visual Recognition
# (https://cs231n.github.io/neural-networks-case-study/)
def classification_data_generator(cantidad_ejemplos, cantidad_clases):
    FACTOR_ANGULO = 0.79
    AMPLITUD_ALEATORIEDAD = 0.1

    # Calculamos la cantidad de puntos por cada clase, asumiendo la misma cantidad para cada 
    # una (clases balanceadas)
    n = int(cantidad_ejemplos / cantidad_clases)

    # Entradas: 2 columnas (x1 y x2)
    x = np.zeros((cantidad_ejemplos, 2))
    # Salida deseada ("target"): 1 columna que contendra la clase correspondiente (codificada como un entero)
    t = np.zeros(cantidad_ejemplos, dtype="uint8")  # 1 columna: la clase correspondiente (t -> "target")

    randomgen = np.random.default_rng()

    # Por cada clase (que va de 0 a cantidad_clases)...
    for clase in range(cantidad_clases):
        # Tomando la ecuacion parametrica del circulo (x = r * cos(t), y = r * sin(t)), generamos 
        # radios distribuidos uniformemente entre 0 y 1 para la clase actual, y agregamos un poco de
        # aleatoriedad
        radios = np.linspace(0, 1, n) + AMPLITUD_ALEATORIEDAD * randomgen.standard_normal(size=n)

        # ... y angulos distribuidos tambien uniformemente, con un desfasaje por cada clase
        angulos = np.linspace(clase * np.pi * FACTOR_ANGULO, (clase + 1) * np.pi * FACTOR_ANGULO, n)

        # Generamos un rango con los subindices de cada punto de esta clase. Este rango se va
        # desplazando para cada clase: para la primera clase los indices estan en [0, n-1], para
        # la segunda clase estan en [n, (2 * n) - 1], etc.
        indices = range(clase * n, (clase + 1) * n)

        # Generamos las "entradas", los valores de las variables independientes. Las variables:
        # radios, angulos e indices tienen n elementos cada una, por lo que le estamos agregando
        # tambien n elementos a la variable x (que incorpora ambas entradas, x1 y x2)
        x1 = radios * np.sin(angulos)
        x2 = radios * np.cos(angulos)
        x[indices] = np.c_[x1, x2]

        # Guardamos el valor de la clase que le vamos a asociar a las entradas x1 y x2 que acabamos
        # de generar
        t[indices] = clase
    
    return x, t


        #-------------------------------------------------------------------------------------------------------#
        #-------------------------------------------------------------------------------------------------------#
        #------------------------------------------------ITEM 4-------------------------------------------------#
        #-------------------------------------------------------------------------------------------------------#
        #-------------------------------------------------------------------------------------------------------#


def classification_data_generator2(cantidad_ejemplos, cantidad_clases):
    AMPLITUD_ALEATORIEDAD = 0.11

    # Calculamos la cantidad de puntos por cada clase, asumiendo la misma cantidad para cada 
    # una (clases balanceadas, lo cual es ideal)
    n = int(cantidad_ejemplos / cantidad_clases) #=300/3=100

    # Entradas: 2 columnas (x1 y x2)
    x = np.zeros((cantidad_ejemplos, 2)) #300 filas x 2 columnas
    # Salida deseada ("target"): 1 columna que contendra la clase correspondiente (codificada como un entero)
    t = np.zeros(cantidad_ejemplos, dtype="uint8")  # 1 columna: la clase correspondiente (t -> "target")

    randomgen = np.random.default_rng()

    # Por cada clase (que va de 0 a cantidad_clases)...
    for clase in range(cantidad_clases): #Son 3 clases
        # Tomando la ecuacion parametrica del circulo (x = r * cos(t), y = r * sin(t)), generamos 
        # radios distribuidos uniformemente entre 0 y 1 para la clase actual, y agregamos un poco de
        # aleatoriedad
        #radios = np.linspace(1, 3, n) + AMPLITUD_ALEATORIEDAD * randomgen.standard_normal(size=n)
        if clase == 0:
            radios = np.linspace(1, 1.55, n) + AMPLITUD_ALEATORIEDAD * randomgen.standard_normal(size=n)
        elif clase == 1:
            radios = np.linspace(1.5, 2.2, n) + AMPLITUD_ALEATORIEDAD * randomgen.standard_normal(size=n)
        elif clase == 2:
            radios = np.linspace(2.1, 2.9, n) + AMPLITUD_ALEATORIEDAD * randomgen.standard_normal(size=n)
        
        # ... y angulos distribuidos tambien uniformemente, con un desfasaje por cada clase
        #angulos = np.linspace(clase * np.pi * FACTOR_ANGULO, (clase + 1) * np.pi * FACTOR_ANGULO, n)
        #angulos = np.linspace((clase*clase) * np.pi * FACTOR_ANGULO, (clase + 1)* np.pi * FACTOR_ANGULO, n)
        angulos = np.linspace(0, 360/((clase+1)*(clase+1)), n)

        # Generamos un rango con los subindices de cada punto de esta clase. Este rango se va
        # desplazando para cada clase: para la primera clase los indices estan en [0, n-1], para
        # la segunda clase estan en [n, (2 * n) - 1], etc.
        indices = range(clase * n, (clase + 1) * n)

        # Generamos las "entradas", los valores de las variables independientes. Las variables:
        # radios, angulos e indices tienen n elementos cada una, por lo que le estamos agregando
        # tambien n elementos a la variable x (que incorpora ambas entradas, x1 y x2)
        x1 = radios * np.sin(angulos) #y
        x2 = radios * np.cos(angulos) #x
        x[indices] = np.c_[x1, x2]

        # Guardamos el valor de la clase que le vamos a asociar a las entradas x1 y x2 que acabamos
        # de generar
        t[indices] = clase

    return x, t


        #-------------------------------------------------------------------------------------------------------#
        #-------------------------------------------------------------------------------------------------------#
        #-------------------------------------------------------------------------------------------------------#
        #-------------------------------------------------------------------------------------------------------#
        #-------------------------------------------------------------------------------------------------------#

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

    w1 = 0.1 * randomgen.standard_normal((n_entrada, n_capa_2))
    b1 = 0.1 * randomgen.standard_normal((1, n_capa_2))

    w2 = 0.1 * randomgen.standard_normal((n_capa_2, n_capa_3))
    b2 = 0.1 * randomgen.standard_normal((1,n_capa_3))

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

    # Funcion de activacion ReLU para la capa oculta (h -> "hidden")
    h = np.maximum(0, z)

    # Salida de la red (funcion de activacion lineal). Esto incluye la salida de todas
    # las neuronas y para todos los ejemplos proporcionados
    y = h.dot(pesos["w2"]) + pesos["b2"]

    return {"z": z, "h": h, "y": y}


def clasificar(x, pesos):
    """Using the results of Forward Propagation, decides the class of the input data.

    Args:
        x (np array): Input data (Features)
        pesos (dictionary): Weights and biases of the neural network

    Returns:
        int: Calculated class of each example in the input data
    """

    # Corremos la red "hacia adelante"
    resultados_feed_forward = ejecutar_adelante(x, pesos)
    
    # Buscamos la(s) clase(s) con scores mas altos (en caso de que haya mas de una con 
    # el mismo score estas podrian ser varias). Dado que se puede ejecutar en batch (x 
    # podria contener varios ejemplos), buscamos los maximos a lo largo del axis=1 
    # (es decir, por filas)
    max_scores = np.argmax(resultados_feed_forward["y"], axis=1)


    # Tomamos el primero de los maximos (podria usarse otro criterio, como ser eleccion aleatoria)
    # Nuevamente, dado que max_scores puede contener varios renglones (uno por cada ejemplo),
    # retornamos la primera columna
    return max_scores

def calculate_accuracy(y,t):
    corrects=np.sum(y==t) 
    total=y.shape[0] 
    accuracy = 100*(corrects) / total
    return accuracy

def Loss(y, t):
    
    """Calculates the loss of the neural network.

    Args:
        y (np array): Output of the neural network
        t (np array): Targets

    Returns:
        int: Total loss of the neural network
    """
    m=np.size(y, 0)
    # a. Exponencial de todos los scores
    exp_scores = np.exp(y)
    # b. Suma de todos los exponenciales de los scores, fila por fila (ejemplo por ejemplo).
    #    Mantenemos las dimensiones (indicamos a NumPy que mantenga la segunda dimension del
    #    arreglo, aunque sea una sola columna, para permitir el broadcast correcto en operaciones
    #    subsiguientes)
    sum_exp_scores = np.sum(exp_scores, axis=1, keepdims=True)

    # c. "Probabilidades": normalizacion de las exponenciales del score de cada clase (dividiendo por 
    #    la suma de exponenciales de todos los scores), fila por fila
    p = exp_scores / sum_exp_scores

    # d. Calculo de la funcion de perdida global. Solo se usa la probabilidad de la clase correcta, 
    #    que tomamos del array t ("target")
    loss = (1 / m) * np.sum( -np.log( p[range(m), t] ))

    return p, loss

def back_propagation(p,x,t,h,z,w2):

    """Calculates changes for weights and biases of the neural network.

    Args:
        p (np array): Probabilities of the classes
        x (np array): Input data (Features)
        t (np array): Targets
        h (np array): Output of the hidden layer
        z (np array): Input of the hidden layer
        w2 (np array): Weights of the output layer

    Returns:
        dL_dw1 (np array): Change in the weights of the input layer
        dL_db1 (np array): Change in the biases of the input layer
        dL_dw2 (np array): Change in the weights of the output layer
        dL_db2 (np array): Change in the biases of the output layer
        
    """

    m=np.size(x, 0)
    dL_dy = p                # Para todas las salidas, L' = p (la probabilidad)...
    dL_dy[range(m), t] -= 1  # ... excepto para la clase correcta
    dL_dy /= m

    dL_dw2 = h.T.dot(dL_dy)                         # Ajuste para w2
    dL_db2 = np.sum(dL_dy, axis=0, keepdims=True)   # Ajuste para b2

    dL_dh = dL_dy.dot(w2.T)
    
    dL_dz = dL_dh       # El calculo dL/dz = dL/dh * dh/dz. La funcion "h" es la funcion de activacion de la capa oculta,
    dL_dz[z <= 0] = 0   # para la que usamos ReLU. La derivada de la funcion ReLU: 1(z > 0) (0 en otro caso)

    dL_dw1 = x.T.dot(dL_dz)                         # Ajuste para w1
    dL_db1 = np.sum(dL_dz, axis=0, keepdims=True)   # Ajuste para b1
    return dL_dw1, dL_db1, dL_dw2, dL_db2

# x: n entradas para cada uno de los m ejemplos(nxm)
# t: salida correcta (target) para cada uno de los m ejemplos (m x 1)
# pesos: pesos (W y b)
# La función actualiza el valor del diccionario pesos
def train(x, t, x_val, t_val, pesos, learning_rate, epochs, N):
    """Changes the weights and biases(all in the dictionary "pesos") of the neural network. 

    Args:
        x (np array): Input data (Features)
        t (np array): Output data (Targets)
        pesos (dictionary): Weights and biases of the neural network
        learning_rate (float): Hyperparameter that determines the pace of change of the weights for each epoch
        epochs (int): Number of epochs to train the neural network
    """

    # Cantidad de filas (i.e. cantidad de ejemplos)
    m = np.size(x, 0) 
    
    
    verify = False
    #m_val = np.size(x_val, 0)
    iteration = 0
    internal_counter = 0
    
    for i in range(epochs):
        # Ejecucion de la red hacia adelante
        resultados_feed_forward = ejecutar_adelante(x, pesos)
        y = resultados_feed_forward["y"]
        h = resultados_feed_forward["h"]
        z = resultados_feed_forward["z"]

        # LOSS
        p, _ = Loss(y, t)
        
        
        #-------------------------------------------------------------------------------------------------------#
        #-------------------------------------------------------------------------------------------------------#
        #------------------------------------------------ITEM 3-------------------------------------------------#
        #-------------------------------------------------------------------------------------------------------#
        #-------------------------------------------------------------------------------------------------------#
        
        if iteration == N:
            iteration = 0

            resultados_feed_forward_validation = ejecutar_adelante(x_val, pesos)
            y_val = resultados_feed_forward_validation["y"]
            _, validation_loss = Loss(y_val, t_val)
            print("Validation loss epoch", i, ":", validation_loss)
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

        #-------------------------------------------------------------------------------------------------------#
        #-------------------------------------------------------------------------------------------------------#
        #-------------------------------------------------------------------------------------------------------#
        #-------------------------------------------------------------------------------------------------------#
        #-------------------------------------------------------------------------------------------------------#


        # Extraemos los pesos a variables locales
        w1 = pesos["w1"]
        b1 = pesos["b1"]
        w2 = pesos["w2"]
        b2 = pesos["b2"]

        # Ajustamos los pesos: Backpropagation
        dL_dw1, dL_db1, dL_dw2, dL_db2=back_propagation(p,x,t,h,z,w2)

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
 

def iniciar(numero_clases, numero_ejemplos, graficar_datos,hidden,learning_rate,epochs,activation):
    """Runs all the NN functions.

    Args:
        numero_clases (int): Number of classes
        numero_ejemplos (int): Number of examples
        graficar_datos (bool): If True, plots the data
    """
    # Generate the data
    x, t = classification_data_generator(numero_ejemplos, numero_clases)
    # Split the data
    x_train,t_train,x_val,t_val=random_extract(x,t,int(numero_ejemplos/5))
    x_train,t_train,x_test,t_test=random_extract(x_train,t_train,int(numero_ejemplos/5))
    #Now we have x_Train,t_Train,x_Val,t_Val,x_Test,t_Test with the right values

    # Graficamos los datos si es necesario
    if graficar_datos:
        # Parametro: "c": color (un color distinto para cada clase en t)
        #Every image in the same plot
        plt.subplot(1,3,1)
        plt.scatter(x_train[:, 0], x_train[:, 1], c=t_train)
        plt.title("Training data ("+str(t_train.shape[0])+"examples)")
        plt.subplot(1,3,2)
        plt.scatter(x_val[:,0], x_val[:,1], c=t_val)
        plt.title("Validation data ("+str(t_val.shape[0])+"examples)")
        plt.subplot(1,3,3)
        plt.scatter(x_test[:,0], x_test[:,1], c=t_test)
        plt.title("Test data ("+str(t_test.shape[0])+"examples)")
        plt.show()

    # Inicializa pesos de la red
    NEURONAS_CAPA_OCULTA = hidden
    NEURONAS_ENTRADA = 2
    pesos = inicializar_pesos(n_entrada=NEURONAS_ENTRADA, n_capa_2=NEURONAS_CAPA_OCULTA, n_capa_3=numero_clases)

    # Entrena
    LEARNING_RATE=learning_rate
    EPOCHS=epochs
    N = 1000
    train(x_train, t_train, x_val, t_val, pesos, LEARNING_RATE, EPOCHS, N)

    #Evaluate the model (our pesos dictionary has been trained)
    y_test=clasificar(x_test,pesos)
    Acc=calculate_accuracy(y_test,t_test)
    print("The model accuracy is: ",Acc,"%")
    return Acc



#Acc=iniciar(numero_clases=3, numero_ejemplos=1000, graficar_datos=True,hidden=100,learning_rate=1,epochs=100000,activation="sigmoid")



#Check if overfitting should consider a little increase temporally
#Accuracy varies too much. We might try fixing the dataset or changing early stop.
#In parameter sweep we should use one dataset, so we take out of the equation the variability in dataset generation.