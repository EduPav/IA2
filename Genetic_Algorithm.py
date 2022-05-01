import csv
import random

from numpy import size
from Simulated_Annealing import simulated_annealing

#Save best example found

# Correct language use
# pep-8
# Si cambias tamaño de la poblacion, cambiar population_premium.
# Be careful. Crossover strongly depends on the population size
#Separate Genetic algorithm from exercise 3
#change layout size to 99
#Selection of only best 3 and mix them (if kill<50% evolution is slow )
#Fitness only using first 10 orders. Correct that. Make them random? representative? all?


order_one = [10, 5, 8, 9, 2, 7, 1, 3, 6, 4]
order_two = [3, 5, 8, 7, 9, 4, 6, 1, 10, 2]
order_three = [3, 5, 8, 7, 9, 4, 6, 1]


def generate_random_individual(layout_size):
    #list of 1,2,3,...98,99
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
       
    Kmax = 10000 #Maximum number of iterations
    Temp0 = 10 #INITIAL TEMPERATURE
    for single_order in order_list:
        _,_,_,best_cost = simulated_annealing(distance_matrix, single_order, Temp0, Kmax)
        total_cost += best_cost
    return total_cost

def crossover(population, population_costs):

    # POPULATION PREMIUM

    # Order population acording to population_costs
    temp_list = [i for _, i in sorted(zip(population_costs, population))]
    temp_cost = sorted(population_costs)

    population = temp_list  # [::-1]
    population_costs = temp_cost  # [::-1]

    for _ in range(2):
        min_idx = population_costs.index(max(population_costs))
        population_costs.pop(min_idx)
        population.pop(min_idx)

    population.append(population[0])
    population.append(population[3])

    population_costs.append(population_costs[0])
    population_costs.append(population_costs[3])

    # CROSSOVER
    juniors = []
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
        print(auxA)
        print(auxB)
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
        return result
    else:
        print("Order doesn't exist")
        return False


def main():
    #Number of annealing runs:  pop_size*time*order_list_size=6*1000*100=600k
    #Number of possible layouts=99! 
    time = 1000  # Max amount of iterations
    layout_size=99
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
    for i in range(1,100): 
        order =read_file("orders.txt", i)
        orders_list.append(order)

    # Generates initial population
    for i in range(population_size):
        population.append(generate_random_individual(layout_size))

    # Print initial population
    #print('\n'.join([''.join(['{:4}'.format(item) for item in row])
    #                 for row in population]))  

    
    #best_individual=
    #best_cost=1000000 #Big enough so its replaced by any layout cost
    generation = 0
    generations_costs=[]
    while generation < time:

        # Calculates the cost of each individual
        for i in range(population_size):
            population_costs.append(fitness(population[i],distance_matrix,orders_list[0:10]))
            generations_costs.append(population_costs[i])

        # Eliminates the last two individuals and make the crossover:
        population = crossover(population, population_costs)

        for j in range(population_size):
            r = random.uniform(0, 1)
            if r<mutation_prob:
                mutation(population[j]) #No need to make population[j]=mut... because mut works with the object

        generation = generation + 1
        population_costs=[]
        


    print("The best warehouse design is: ")
    print('\n'.join([''.join(['{:4}'.format(item) for item in row])
                     for row in population])) 

    print(generations_costs)


if __name__ == '__main__':
    main()
