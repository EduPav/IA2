import csv
import random
from Simulated_Annealing import simulated_annealing
import matplotlib.pyplot as plt
import numpy as np

#Save best example found
# pep-8
#Separate Genetic algorithm from exercise 3


def generate_random_individual(layout_size):
    """_summary_

    Args:
        layout_size (_type_): _description_

    Returns:
        _type_: _description_
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
    for single_order in order_list:
        _,_,_,best_cost = simulated_annealing(distance_matrix, single_order, Temp0, Kmax)
        total_cost += best_cost
    return total_cost

def crossover(population, population_costs):
    """_summary_

    Args:
        population (_type_): _description_
        population_costs (_type_): _description_
    """

    # POPULATION PREMIUM
#PRUEBA N°1:
    # Order population acording to population_costs
    #temp_list = [i for _, i in sorted(zip(population_costs, population))]
    #temp_cost = sorted(population_costs)

    #population = temp_list  # [::-1]
    #population_costs = temp_cost  # [::-1]

    #for _ in range(2):
    #    min_idx = population_costs.index(max(population_costs))
    #    population_costs.pop(min_idx)
    #    population.pop(min_idx)

   # population.append(population[0])
   # population.append(population[3])

   # population_costs.append(population_costs[0])
   # population_costs.append(population_costs[3])
    

#PRUEBA N°2:
    #prob = [0.858, 0.716, 0.574, 0.432, 0.29, 0.148]

    # Order population acording to population_costs
    # for i in range(len(population_costs)):
    #    population_costs[i] = 1/population_costs[i]
    # #print(population_costs)
    
    # population = random.choices(population, weights=prob, k=6)
    # population_1 = random.choices(population, weights=prob, k=6)

    # for i in range(0, len(population), 2):
    #    if population[i] == population[i+1]:
    #        for j in range(len(population)):
    #            if population[i+1] != population_1[j]:
    #                population[i+1] = population_1[j]
    #                break

#PRUEBA N°3:
    # Order population acording to population_costs
    for i in range(len(population_costs)):
        population_costs[i] = 1/population_costs[i]
    #print(population_costs)
    
    population = random.choices(population, weights=population_costs, k=6)
    population_1 = random.choices(population, weights=population_costs, k=6)

    for i in range(0, len(population), 2):
        if population[i] == population[i+1]:
            for j in range(len(population)):
                if population[i+1] != population_1[j]:
                    population[i+1] = population_1[j]
                    break


    # CROSSOVER
    juniors = []
    prueba = population[1]
    for i in range(0, len(population), 2):
        # print(len(population))
        individual_length = len(population[0])
        junior1 = [0]*individual_length
        junior2 = [0]*individual_length

        a = random.randint(0, individual_length-2)
        b = random.randint(a+1, individual_length-1)
        auxA = population[i][a:b]
        auxB = population[i+1][a:b]

        junior1[a:b] = auxB
        junior2[a:b] = auxA
        #print(auxA)
        #print(auxB)
        j = 0
        k = 0

        while j < (individual_length):

            for k in range(individual_length):
                if j < a or j >= b:

                    if population[i][k] not in junior1:
                        junior1[j] = population[i][k]
                        j = j + 1
                        k = 0
                else:
                    j = j + 1

                if j == (individual_length):
                    break
        j = 0
        k = 0
        while j < (individual_length):

            for k in range(individual_length):
                if j < a or j >= b:
                    if population[i+1][k] not in junior2:
                        junior2[j] = population[i+1][k]
                        j = j + 1
                        k = 0

                else:
                    j = j + 1

                if j == (individual_length):
                    break
        # if i == 1:
        #     juniors.append(prueba)
        #     juniors.append(junior2)
        # else:
        #     juniors.append(junior1)
        #     juniors.append(junior2)
        juniors.append(junior1)
        juniors.append(junior2)

    return juniors


def mutation(individual):
    random_a = random.randint(0, len(individual)-1)
    random_b = random.randint(0, len(individual)-1)
    while(random_b==random_a):
        random_b = random.randint(0, len(individual)-1) #To guarantee mutation occurs

    individual_a = individual[random_a]
    individual_b = individual[random_b]

    individual[random_b] = individual_a
    individual[random_a] = individual_b

    return individual

def read_file(filename, order_number):
    """
    Read "filename" file to return the "order_number" products list

    Args:
        filename (string): Name of the file to read
        order_number (int): Number of order to read from the file

    Returns:
        list: List of products for one order
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
    itmax = 100  # Max amount of iterations
    layout_size=100
    #original layout: [1,2,3,4,5,6,7,8,....,98,99]
    population_size = 6 
    population = []
    population_costs = []
    mutation_prob = 0.01  #mutation probability

    with open('distance_matrix.csv') as csvfile:
        rows = csv.reader(csvfile)
        distance_matrix = list(zip(*rows))
    #Distance matrix is now a list of tuples of STRINGS

    #Put all orders in a list
    orders_list=[]
    for i in range(1,100): #nº of orders
        order =read_file("orders.txt", i)
        orders_list.append(order)

    # Generates initial population
    for i in range(population_size):
        population.append(generate_random_individual(layout_size))
        

    # Print initial population
    #print('\n'.join([''.join(['{:4}'.format(item) for item in row])
    #                 for row in population]))  

    
    #best_individual=
    best_cost=1000000 #Big enough so its replaced by any layout cost
    generation = 0
    historical_costs=[]
    while generation < itmax:
        generations_costs=[]
        # Calculates the cost of each individual
        for i in range(population_size):
            population_costs.append(fitness(population[i],distance_matrix,orders_list[0:100]))
            generations_costs.append(population_costs[i])
            if best_cost>population_costs[i]:
                best_indiv=population[i]
                best_cost=population_costs[i]
            
        historical_costs.append(generations_costs)
        if generation == 0:
            print(generations_costs) #Print costs of starting random generation
        # Eliminates the last two individuals and make the crossover:
        population = crossover(population, population_costs)

        for j in range(population_size):
            r = random.uniform(0, 1)
            if r<mutation_prob:
                mutation(population[j]) #No need to make population[j]=mut... because mut works with the object

        generation = generation + 1
        print(generation)
        population_costs=[]
        


    
    print("The best layout found is:"+str(best_indiv))
    print("Its cost is: "+str(best_cost))

    #Ploting costs evolution during generations
    individ=[]

    for i in range(6):
        individ.append([generation[i]for generation in historical_costs])
    print(generations_costs)
    x=np.arange(0.,itmax)
    plt.plot(x,individ[0],'*',x,individ[1],'*',x,individ[2],'*',x,individ[3],'*',x,individ[4],'*',x,individ[5],'*')
    plt.show()
    
    #I don't think this is going to work with our individual structure
    #print("The best warehouse design is: ")
    #print('\n'.join([''.join(['{:4}'.format(item) for item in row])
    #                 for row in population])) 
    


if __name__ == '__main__':
    main()




