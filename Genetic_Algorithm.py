import random
import math
# Correct language use
# pep-8
# Klaga: Build generate random individual function of python so it's more efficient.
# Si cambias tamaño de la poblacion, cambiar population_premium.
# Use premium inside crossover function. (LISTO)        (Be careful. Crossover strongly depends on the population size)
# Corrige Agus para cruce de orden. (LISTO)


order_one = [10, 5, 8, 9, 2, 7, 1, 3, 6, 4]
order_two = [3, 5, 8, 7, 9, 4, 6, 1, 10, 2]


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


def fitness(population_size):
    pass


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
