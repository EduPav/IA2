import random
import math


dictionary = {1:[0,1], 2:[0,2], 3:[2,0], 4:[2,3], 5:[3,0], 6:[3,3], 7:[4,0], 8:[4,3], 9:[6,0], 10:[6,3], 11:[7,0], 12:[7,3], 13:[8,0], 14:[8,3], 15:[9,0], 16:[9,3], 17:[11,0], 18:[11,3], 19:[12,0], 20:[12,3], 21:[13,0], 22:[13,3], 23:[14,0], 24:[14,3]}
#Despues cambiar dictionary (ahora esta puesto para que no de error)
Kmax = 10000 #Maximum number of iterations
TO = T = 10 #INITIAL TEMPERATURE
Old_a = 9999 #initial value of Old_a



def Random_Permutation(order_list):
    """Asks for the actual order list. Returns a new order list"""
    random_a = random.randint(1, len(order_list)-1)
    random_b = random.randint(1, len(order_list)-1)
    #print(random_a)
    order_a = order_list[random_a]
    order_b = order_list[random_b]

    order_list[random_b] = order_a
    order_list[random_a] = order_b

    return order_list

def temperature(TO, k):
    """Asks for the initial temperature and the acrual iteration. Returns reduced temperature"""
    T = TO*pow((0.99),k) #0.99 is the cooling rate
    return T

def probability(New_Cost, Actual_Cost, T):
    """Asks for the new and actual cost of the picking secuence and the temperature. Returns the probability of accepting a bad neighbor"""
    prob = math.exp(-(New_Cost-Actual_Cost)/T)
    return prob

def Total_cost_of (orders, maze):
    """Returns the picking secuence cost"""
    for i in range(len(orders)):

            if i == 0:
                start_position = dictionary[orders[i]]
                
            else:
                start_position = dictionary[orders[i-1]]
                
            #print(i)
            a += prueba_Borrar.algorithm(maze, dictionary[orders[i]], start_position)  #Prueba_Borrar is the A_Star algorythm module (cambiar al nombre correcto cuando esté creado)
    return a

def Simulated_Annealing(maze, orders):
    """Returns the best picking secuence"""
    for counter in range(Kmax):
        a=0
        New_orders = Random_Permutation(orders)  #Generate a neighbor
        
        a = Total_cost_of(New_orders, maze)

        if a < Old_a:
            orders = New_orders
            Old_a = a
        else:
            r = random.uniform(0, 1)
            prob = probability(a, Old_a, T) #Probability of accepting the neighbor

            if prob >= r:
                orders = New_orders
                Old_a = a
            else:
                orders = orders

        T=temperature(TO, counter) #Reduces temperature
        
        
    
    return orders #Best picking sequence


def main():
    print("This is the main")


if __name__ == '__main__':
    main()
#REVISAR PROBABILIDAD DE ACEPTAR UN VECINO MALO