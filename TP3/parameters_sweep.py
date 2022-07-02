import numpy as np
from MLP_Classification_kfold import iniciar
from MLP_Classification_kfold import classification_data_generator

#Learning rates, sigmoid and relu, hidden layer neurons

learning_rates=[0.01,0.05,0.1,0.5,1,2,5,10]
h_sizes=[10,30,60,100,150,200]
# activation=["relu","sigmoid"]


#RANDOM SEARCH
#Total posible combinations=2*8*6=96

total_it=20 #per activation function
#Pick random combinations of a learning rate, a hidden number of neurons and an activation function without repetition
used=[]
accuracy_list=[]
# act="relu"

x, t = classification_data_generator(cantidad_ejemplos=1000, cantidad_clases=3)


#for act in activation:
for i in range(total_it):
    axis1=np.random.randint(0,len(learning_rates),1)
    axis2=np.random.randint(0,len(h_sizes),1)
    if (axis1,axis2) in used:
        continue
    used.append((axis1,axis2))
    learning_rate=learning_rates[axis1[0]]
    h_size=h_sizes[axis2[0]]
    print("learning_Rate=",learning_rate,"///hidden_layer_size=",h_size)
    accuracy_list.append(iniciar(x,t,graficar_datos=False,hidden=h_size,learning_rate=learning_rate,epochs=10000,K=3))       

#Get best accuracy index and show which used values were used
best_accuracy_index=np.argmax(accuracy_list)
best_learning_rate=learning_rates[used[best_accuracy_index][0][0]]
best_h_size=h_sizes[used[best_accuracy_index][1][0]]
print("Best accuracy=",accuracy_list[best_accuracy_index],"///Best learning_rate=",best_learning_rate,"///Best hidden_layer_size=",best_h_size)
