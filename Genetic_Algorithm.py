import random
import math

order_one = [10, 5, 8, 9, 2, 7, 1, 3, 6, 4]
order_two = [3, 5, 8, 7, 9, 4, 6, 1, 10, 2]

def generate_warehouse_layout(lista_original):

    lista = lista_original[:]
    longitud_lista = len(lista)
    for i in range(longitud_lista):
        
        indice_aleatorio = random.randint(0, longitud_lista - 1)
        # Exchange
        temporal = lista[i]
        lista[i] = lista[indice_aleatorio]
        lista[indice_aleatorio] = temporal
    
    return lista

def fitness(population):

    pass

def Population_Premium(population_layout, population_cost):  #Elimina los últimos 2 valores

    result_list = [i for _,i in sorted(zip(population_cost,population_layout))]  #Ordena population_layout de acuerdo a population_cost
    result_cost = sorted(population_cost)

    population_layout = result_list[::-1]
    population_cost = result_cost[::-1]

    for i in range(2):
        min = population_cost.index(min(population_cost))
        population_cost.pop(min)
        population_layout.pop(min)

    population_layout.append(population_layout[0])
    population_layout.append(population_layout[3])

    population_cost.append(population_cost[0])
    population_cost.append(population_cost[3])

    return population_layout, population_cost

def crossover(population_layout):
    hijos = []
    for i in range( 0, len(population_layout), 2):
        hijo1 = [0]*len(population_layout[0])
        hijo2 = [0]*len(population_layout[0])
        a = random.randint(0, len(population_layout[0])-1)
        b = random.randint(a, len(population_layout[0])-1)
        auxA = population_layout[i][a:b+1]
        auxB = population_layout[i+1][a:b+1]

        hijo1[a:b] = auxB
        hijo1[a:b] = auxA
        j = 0
        while j < (len(population_layout[0])):
            
            if j<a or j>b:
                numA = random.randint(0, len(population_layout[0])-1)
                numB = random.randint(0, len(population_layout[0])-1)
                if numA not in hijo1 and numB not in hijo2:
                    hijo1[j]=numA
                    hijo2[j]=numB
                    j= j + 1
            
            else: 
                j = j+1
        hijos.append(hijo1)
        hijos.append(hijo2)
    

def mutation(individual):
    random_a = random.randint(0, len(individual)-1)
    random_b = random.randint(0, len(individual)-1)
    #print(random_a)
    order_a = individual[random_a]
    order_b = individual[random_b]

    individual[random_b] = order_a
    individual[random_a] = order_b

    return individual

def main():
    time = 1000 #Max amount of iterations

    original_layout = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    population = 6
    population_layout = []
    population_cost = []
    mutation_prob = 0.01 #mutation probability


    #Genera la población
    for i in range(population):
        population_layout.append(generate_warehouse_layout(original_layout))
    
    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
      for row in population_layout]))  #Print the matrix


    #Calcula el "costo" de cada ordenamiento
    for i in range(population):
        population_cost[i].append(fitness(population_layout[i]))

    
    population_layout, population_cost = Population_Premium(population_layout, population_cost) #Elimina los últimos 2 valores





if __name__ == '__main__':
    main()