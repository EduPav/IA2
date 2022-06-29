import numpy as np
from MLP_Classification import iniciar

#Learning rates, sigmoid and relu, hidden layer neurons

learning_rates=[0.01,0.05,0.1,0.5,1,2,5,10]
h_sizes=[10,30,60,100,150,200]
activation=["relu","sigmoid"]

#make 3d plots showing for each activation function the performance reached 
#Early stop

#RANDOM SEARCH
#Total posible combinations=2*8*6=96

total_it=20 #per activation function
#Pick random combinations of a learning rate, a hidden number of neurons and an activation function without repetition
used=[]
accuracy_list=[]
for act in activation:
    for i in range(total_it):
        axis1=np.random.randint(0,len(learning_rates),1)
        axis2=np.random.randint(0,len(h_sizes),1)
        if (act,axis1,axis2) in used:
            continue
        used.append((act,axis1,axis2))
        learning_rate=learning_rates[axis1]
        h_size=h_sizes[axis2]
        accuracy_list.append(iniciar(numero_clases=3, numero_ejemplos=1000, graficar_datos=True,hidden=h_size,learning_rate=learning_rate,epochs=10000,activation=act))        


    
