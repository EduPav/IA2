import csv
import random
import math
import Simulated_Annealing
# Correct language use
# pep-8
# Klaga: Build generate random individual function of python so it's more efficient.
# Si cambias tamaño de la poblacion, cambiar population_premium.
# Use premium inside crossover function. (LISTO)        (Be careful. Crossover strongly depends on the population size)
# Corrige Agus para cruce de orden. (LISTO)


order_one = [10, 5, 8, 9, 2, 7, 1, 3, 6, 4]
order_two = [3, 5, 8, 7, 9, 4, 6, 1, 10, 2]
order_three = [3, 5, 8, 7, 9, 4, 6, 1]


def generate_random_individual(lista_original):

    lista = lista_original[:]
    longitud_lista = len(lista)
    for i in range(longitud_lista):

        indice_aleatorio = random.randint(0, longitud_lista - 1)
        # Exchange
        temporal = lista[i]
        lista[i] = lista[indice_aleatorio]
        lista[indice_aleatorio] = temporal

    return lista


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


def fitness(individual):
    """calculates the cost of orders for each order, for one individual

    Args:
        individual (list): warehouse layout

    Returns:
        int: total cost of orders
    """
    order_list = []
    total_cost = 0
    
    with open('distance_matrix.csv') as csvfile:
        rows = csv.reader(csvfile)
        distance_matrix = list(zip(*rows))
    #Distance matrix is now a list of tuples of STRINGS

    #uncomment when individual list is all of products
    # for i in range(1,100): 
        # order = Simulated_Annealing.read_file("orders.txt", i)
        # order_list.append(filter_order(order, individual))
    order_list.append(filter_order(order_three, individual))#to test, delete when individual list is all of products
    
    Kmax = 10000 #Maximum number of iterations
    Temp0 = 10 #INITIAL TEMPERATURE
    for i in order_list:
        _,_,_,best_cost = Simulated_Annealing.simulated_annealing(distance_matrix, i, Temp0, Kmax)
        total_cost += best_cost
    
    print("total cost =", total_cost)
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
    # print(random_a)
    individual_a = individual[random_a]
    individual_b = individual[random_b]

    individual[random_b] = individual_a
    individual[random_a] = individual_b

    return individual


def main():
    time = 1000  # Max amount of iterations

    original_layout = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    population_size = 6
    population = []
    population_costs = []
    mutation_prob = 0.01  # mutation probability

    # Generates initial population
    for i in range(population_size):
        population.append(generate_random_individual(original_layout))

    # Print initial population
    print('\n'.join([''.join(['{:4}'.format(item) for item in row])
                     for row in population]))  

    
    generation = 0
    while generation < time:

        # Calculates the cost of each individual
        for i in range(population_size):
            population_costs.append(fitness(population[i]))

        # Eliminates the last two individuals and make the crossover:
        population = crossover(population, population_costs)

        for j in range(population_size):
            r = random.uniform(0, 1)
            if mutation_prob > r:
                population[j] = mutation(population[j])

        generation = generation + 1


    print("The best warehouse design is: ")
    print('\n'.join([''.join(['{:4}'.format(item) for item in row])
                     for row in population])) 



if __name__ == '__main__':
    main()
