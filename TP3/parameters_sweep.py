import numpy as np
from MLP_Clasificacion import iniciar

#Learning rates, sigmoid and relu, hidden layer neurons

learning_rates=[0.01,0.05,0.1,0.5,1,2,5,10]
h_sizes=[10,30,60,100,150,200]
activation=["ReLU","Sigmoid"]

#make 3d plots showing for each activation function the performance reached 
#Early stop

#RANDOM SEARCH
#Total posible combinations=2*8*6=96

total_it=20 #per activation function
#Pick random combinations of a learning rate, a hidden number of neurons and an activation function without repetition
for act in activation:
    for i in range(total_it):
        axis1=np.random.randint(0,len(learning_rates),1)
        axis2=np.random.randint(0,len(h_sizes),1)
        learning_rate=learning_rates[axis1]
        h_size=h_sizes[axis2]
        


    
