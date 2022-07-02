import csv
import random
from Simulated_Annealing import simulated_annealing
import matplotlib.pyplot as plt
import numpy as np



def generate_random_individual(layout_size):
    """
    Returns a list of products corresponding to an individual

    Args:
        layout_size (int): cantidad de productos

    Returns:
        list[int]: list of products
    """
    #list of 1,2,3,...98,99,100
    individual = list(range(layout_size+1))
    individual.pop(0)

    for i in range(layout_size):

        rand_idx = random.randint(0, layout_size - 1)
        # Exchange
        temp = individual[i]
        individual[i] = individual[rand_idx]
        individual[rand_idx] = temp

    return individual

def filter_order(order_sequence, individual):
    """converts the order sequence for it to correspond to the distance matrix calculated before and avoid using a* multiple times

    Args:
        order_sequence (list): list of orders of products
        individual (list): current product warehouse layout

    Returns:
        list: list of orders convert to new warehouse layout
    """
    filtered_order = []
    for i in order_sequence:
        filter = individual.index(i)+1
        filtered_order.append(filter)
    return filtered_order

def fitness(individual,distance_matrix,orders_to_test):
    """calculates the cost of orders for each order, for one individual

    Args:
        individual (list): warehouse layout

    Returns:
        int: total cost of orders
    """
    order_list = []
    total_cost = 0
    order_list=[filter_order(order, individual) for order in orders_to_test]
    
    Kmax = 1000 #Maximum number of iterations
    Temp0 = 25 #INITIAL TEMPERATURE
    cost_per_order=[]
    for single_order in order_list:
        _,_,_,best_cost = simulated_annealing(distance_matrix, single_order, Temp0, Kmax)
        cost_per_order.append(best_cost)
        total_cost += best_cost
    return total_cost,cost_per_order

def read_file(filename, order_number):
    """
    Read "filename" file to return the "order_number"º products list
    filename: string->Name of the file to read
    order_number: int->Number of order to read from the file.
    """
    result = []
    tmp = []
    if order_number >= 0 and order_number <= 100:
        command = "Order " + str(order_number)
        with open(filename, 'r') as f:
            for line in f:
                tmp.append(line.strip()) #Build list of every line in the archive
        index_command = tmp.index(command)+1 #Get the index where the order specified starts
        tmp = tmp[index_command:]   #Cut from the list the previous lines to the specified order
        i = 0
        while i < len(tmp):
            if(tmp[i] == ''):
                break
            i+=1
        tmp = tmp[0:i] #Now tmp is the list of products in the specified order
        for elem in tmp:
            result.append(int(elem.replace("P", ""))) #Transform every product from string "Px" into int x
            if 0 in result:
                result[result.index(0)]=100
        return result
    else:
        print("Order doesn't exist")
        return False

def main():
    #Number of annealing runs:  pop_size*itmax*order_list_size=6*1000*100=600k
    #Number of possible layouts=99! 
    layout_size=100
    #original layout: [1,2,3,4,5,6,7,8,....,98,99]
    population_size = 6 
    population = []


    with open('TP1/Exercise_3/distance_matrix.csv') as csvfile:
        rows = csv.reader(csvfile)
        distance_matrix = list(zip(*rows))
    #Distance matrix is now a list of tuples of STRINGS

    #Put all orders in a list
    orders_list=[]
    for i in range(1,101): #nº of orders
        order =read_file("TP1/Exercise_3/orders.txt", i)
        orders_list.append(order)

    # Generates initial population
    x=[i+1 for i in range(100)]
    fig, axs = plt.subplots(2, 3)
    for i in range(population_size):
        population.append(generate_random_individual(layout_size))
        #print(population[i])
        Tcost,orders_costs=fitness(population[i],distance_matrix,orders_list[0:100])
        print(Tcost)
        orders_costs=np.array(orders_costs)*100/Tcost
        if i==0:
            ref_costs=orders_costs.copy()
        else:
            orders_costs-=ref_costs
        
        if i<=2:
            axs[0, i].bar(x, orders_costs)
            axs[0, i].set_title('Random Individual '+str(i+1))
            if i==0:
                axs[0, i].set(xlabel='Orders', ylabel='Percentage respect total cost')
            else:
                axs[0, i].set(xlabel='Orders', ylabel='Percentage variation respect first plot')
            
        else:
            axs[1, i-3].bar(x, orders_costs)
            axs[1, i-3].set_title('Random Individual '+str(i+1))
            axs[1, i-3].set(xlabel='Orders', ylabel='Percentage variation respect first plot')
    fig.suptitle('Influence of each order cost over the total cost of an individual',size=30)
    plt.show() 


if __name__ == '__main__':
    main()




