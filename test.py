import random
def mutation(individual):
    random_a = random.randint(0, len(individual)-1)
    random_b = random.randint(0, len(individual)-1)
    while(random_b==random_a):
        random_b = random.randint(0, len(individual)-1)

    individual_a = individual[random_a]
    individual_b = individual[random_b]

    individual[random_b] = individual_a
    individual[random_a] = individual_b

    return individual
a=[[1,2],2,3,4]
mutation(a[0])
print(a)
print("Develop branch")
