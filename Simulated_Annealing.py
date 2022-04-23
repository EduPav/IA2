import random
import math
import csv

#As we read distance matrix from archive we don't need a_star or the maze here.
#We only receive lists of products and know where they are in the maze.
#Try changing number of total iterations in sim anealing to see if it's worth getting to that low temperature.
#Be careful with temperature. It might have certain relationship with the real cost, or the cost evolution.
#We will have to print costs vs iterations
#Add input parameters in docstrings at start of each function
#Start variables and functions with lowercase (search for pep8) and snake notation
#REVISAR PROBABILIDAD DE ACEPTAR UN VECINO MALO
#Write all docstrings in infinitive
#Print the maze at least once? Without the paths.
#Change cooling schedule (temperature function) #Nos interesa menos que lineal si la superficie es escarpada. Arrancar con lineal. Si es erratico es escarpada.
#Could avoid entering number of iteration if makes T=T*0,99

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

def temperature(TO, k): 
    """
    Define cooling schedule. 
    Return new temperature given the number of iteration and T0
    T0: int-> starting temperature
    k: int-> number of iteration
    """
    T = TO*pow((0.99),k) #0.99 is the cooling rate T0*0,99^k
    return T

def probability(new_cost, current_cost, T):
    """
    Return int-> probability of accepting a worse neighbor
    new_cost: int-> cost of neighbour sequence
    current_cost: int-> cost of current sequence
    """
    prob = math.exp(-(new_cost-current_cost)/T)
    return prob

def total_cost_of (sequence, distances):
    """
    Return    int->picking up sequence total cost
    sequence  list-> sequence of products
    distances list of lists->distance_matrix with lower costs of traveling between each pair of products
    """
    total_cost=0
    for i in range(len(sequence)-1):        
        total_cost+=distances[sequence[i]][sequence[i+1]]
    return total_cost


def simulated_annealing(distances, sequence,T0,Kmax):
    """
    Return list->Best picking sequence found
    distances: list of lists->distance_matrix with lower costs of traveling between each pair of products
    sequence:  list-> starting sequence
    T0: int->starting temperature
    Kmax: int->max number of iterations
    """
    T=T0
    for counter in range(Kmax):
        previous_cost=total_cost_of(sequence,distances)
        New_sequence = random_permutation(sequence)  #Generate a neighbor
        
        current_cost = total_cost_of(New_sequence, distances)

        if current_cost < previous_cost:
            sequence = New_sequence
            previous_cost = current_cost
        else:
            r = random.uniform(0, 1)
            prob = probability(current_cost, previous_cost, T) #Probability of accepting the neighbor

            if prob >= r: #If not keeps last sequence
                sequence = New_sequence
                previous_cost = current_cost

        T=temperature(T0, counter) #Reduces temperature
        
    
    return sequence #Best picking sequence


def main():
    #it=input("Insert number of random initializations")
    #In case we want to run it with random initializations
    with open('distance_matrix.csv') as csvfile:
        rows = csv.reader(csvfile)
        Distance_matrix = list(zip(*rows))
    #Distance matrix is now a list of tuples

    order = read_file("orders.txt", int(input("Insert order number : ")))
    print(order)
    
    Kmax = 10000 #Maximum number of iterations
    Temp0 = 10 #INITIAL TEMPERATURE
    simulated_annealing(Distance_matrix,order,Temp0,Kmax)
    print(Distance_matrix)
    print("This is the main")
    print("The sequence is:")
    print("The cost is: ")


if __name__ == '__main__':
    main()
