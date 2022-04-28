import random
import math

#As we read distance matrix from archive we don't need a_star or the maze here.



def random_permutation(order_list):
    """
    Return a neighbour sequence (list) with one permutation of the input one.
    order_list: list->Sequence of products 
    """
    random_a = random.randint(1, len(order_list)-1)  
    random_b = random.randint(1, len(order_list)-1)
    while(random_a==random_b): #So it doesn't pick the same product in the sequence twice
        random_b = random.randint(1, len(order_list)-1)


    prod_a = order_list[random_a]
    prod_b = order_list[random_b]

    order_list[random_b] = prod_a
    order_list[random_a] = prod_b

    return order_list

def temperature(Temp,dT): 
    """
    Linear cooling schedule
    Return new temperature(float)
    Temp: float-> current Temperature
    Kmax: int-> Max number of iterations
    """
    Temp = Temp-dT
    return Temp

def probability(new_cost, current_cost, T):
    """
    Return float-> probability of accepting a worse neighbor
    new_cost: int-> cost of neighbour sequence
    current_cost: int-> cost of current sequence
    """
    prob = math.exp(-(new_cost-current_cost)/T) #Bigger cost difference reduces prob. Bigger Temp increases prob
    return prob

def total_cost_of (sequence, distances):
    """
    Return    int->picking up sequence total cost

    sequence  list-> sequence of products

    distances list of lists->distance_matrix with lower costs of traveling between each pair of products
    """
    total_cost=0
    total_cost+=int(distances[2][sequence[0]-1]) #We assume cargo bay in the same picking position of product 3 in the maze (its left)
    for i in range(len(sequence)-1):        
        total_cost+=int(distances[sequence[i]-1][sequence[i+1]-1]) #minus one because product n is row n-1
    total_cost+=int(distances[sequence[i+1]-1][2])
    return total_cost

def simulated_annealing(distances, sequence,T,Kmax):
    """
    Return list->Best picking sequence found and int->cost of that sequence
    distances: list of lists->distance_matrix with lower costs of traveling between each pair of products
    sequence:  list-> starting sequence
    T: float->starting temperature
    Kmax: int->max number of iterations
    """
    costs_evolution=[]
    probs=[]
    current_cost=total_cost_of(sequence,distances)
    best_cost=current_cost
    best_sequence=sequence.copy()
    costs_evolution.append(current_cost)
    dT=T/Kmax
    for _ in range(Kmax):
        new_sequence = random_permutation(sequence)  #Generate a neighbor.It can't be itself.
        new_cost = total_cost_of(new_sequence, distances)
        if new_cost < current_cost:
            sequence = new_sequence
            current_cost = new_cost
            if current_cost<best_cost:
                best_sequence=new_sequence.copy() #.copy() so it's not changed when we change new_sequence
                best_cost=current_cost
                
        else:
            r = random.uniform(0, 1)
            prob = probability(new_cost, current_cost, T) #Probability of accepting the neighbor
            probs.append(prob)
            if r<=prob: #If not keeps last sequence
                sequence = new_sequence
                current_cost = new_cost

        T=temperature(T, dT) #Reduces temperature
        costs_evolution.append(current_cost)
    return probs,costs_evolution,best_sequence,best_cost #Best picking sequence and its cost

