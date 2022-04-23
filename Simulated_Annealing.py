import random
import math
import csv
import matplotlib.pyplot as plt

#As we read distance matrix from archive we don't need a_star or the maze here.
#We only receive lists of products and know where they are in the maze.
#Add input parameters in docstrings at start of each function
#Print the maze at least once? Without the paths.
#Change cooling schedule (temperature function) #Nos interesa menos decrecimiento que lineal si la superficie es escarpada. Arrancar con lineal. Si es erratico es escarpada.
#Maybe not necessity to move from linear. In our case probability is still big at the end in most cases before settling down to a local optimum

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
    for i in range(len(sequence)-1):        
        total_cost+=int(distances[sequence[i]-1][sequence[i+1]-1]) #minus one because product n is row n-1
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
    for counter in range(Kmax):
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

def plot_costs(costs_list):
    """
    Plot the costs list vs its place in the list
    costs_list: list-> Cost values
    """
    plt.plot(costs_list, color='magenta', marker='o' ) #plot the data

    plt.ylabel('costs') #set the label for y axis
    plt.xlabel('iteration') #set the label for x-axis
    plt.title("Simulated annealing") #set the title of the graph
    plt.show() #display the graph

def plot_probs(probs_list):
    """
    Plot the probs list vs its place in the list
    probs_list: list-> probability values
    """
    plt.plot(probs_list, color='magenta', marker='o' ) #plot the data

    plt.ylabel('Probability') #set the label for y axis
    plt.xlabel('Iteration') #set the label for x-axis
    plt.title("Simulated annealing") #set the title of the graph
    plt.show() #display the graph

def main():
    #it=input("Insert number of random initializations")
    #In case we want to run it with random initializations
    with open('distance_matrix.csv') as csvfile:
        rows = csv.reader(csvfile)
        distance_matrix = list(zip(*rows))
    #Distance matrix is now a list of tuples of STRINGS

    #order = read_file("orders.txt", int(input("Insert order number : ")))
    order = read_file("orders.txt", 5)
    print("Order to analize: "+str(order))
    
    Kmax = 10000 #Maximum number of iterations
    Temp0 = 10 #INITIAL TEMPERATURE
    probs,costs_evolution,best_sequence,best_cost=simulated_annealing(distance_matrix,order,Temp0,Kmax)
    print("The best sequence found is:"+str(best_sequence))
    print("Its cost is: "+str(best_cost))
    plot_costs(costs_evolution)
    plot_probs(probs)
    


if __name__ == '__main__':
    main()
