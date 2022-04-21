from asyncore import read
import random
import math
import csv

#As we read distance matrix from archive we don't need a_star or the maze here.
#We only receive lists of proucts and know where they are in the maze.
#Try changing number of total iterations in sim anealing to see if it's worth getting to that low temperature.
#Be careful with temperature. It might have certain relationship with the real cost, or the cost evolution.
#We will have to print costs vs iterations
#Add input parameters in docstrings at start of each function
#Start variables and functions with lowercase (search for pep8) and snake notation

#dictionary = {1:[0,1], 2:[0,2], 3:[2,0], 4:[2,3], 5:[3,0], 6:[3,3], 7:[4,0], 8:[4,3], 9:[6,0], 10:[6,3], 11:[7,0], 12:[7,3], 13:[8,0], 14:[8,3], 15:[9,0], 16:[9,3], 17:[11,0], 18:[11,3], 19:[12,0], 20:[12,3], 21:[13,0], 22:[13,3], 23:[14,0], 24:[14,3]}
#Despues cambiar dictionary (ahora esta puesto para que no de error)

def read_file(filename, order_number):
    """Read file to get product list"""
    result = []
    tmp = []
    if order_number <= 100:
        command = "Order " + str(order_number)
        with open(filename, 'r') as f:
            for line in f:
                tmp.append(line.strip())
        index_command = tmp.index(command)+1
        tmp = tmp[index_command:]
        i = 0
        while i < len(tmp):
            if(tmp[i] == ''):
                break
            i+=1
        tmp = tmp[0:i]
        for elem in tmp:
            result.append(int(elem.replace("P", "")))
        return result
    else:
        print("Order doesn't exist")
        return False


def Random_Permutation(order_list):
    """Asks for an sequence. Returns a neighbour sequence with one permutation"""
    random_a = random.randint(1, len(order_list)-1)
    random_b = random.randint(1, len(order_list)-1)

    order_a = order_list[random_a]
    order_b = order_list[random_b]

    order_list[random_b] = order_a
    order_list[random_a] = order_b

    return order_list

def temperature(TO, k): #Nos interesa menos que lineal si la superficie es escarpada. Arrancar con lineal. Si es erratico es escarpada.
    """Asks for the initial temperature and the current iteration. Returns reduced temperature"""
    T = TO*pow((0.99),k) #0.99 is the cooling rate T0*0,99^k
    return T

def probability(New_Cost, current_Cost, T):
    """Asks for the new and current cost of the picking secuence and the temperature. Returns the probability of accepting a bad neighbor"""
    prob = math.exp(-(New_Cost-current_Cost)/T)
    return prob

def Total_cost_of (sequence, distances):
    """Returns the picking sequence cost"""
    Tcost=0
    for i in range(len(sequence)-1):        
        Tcost+=distances[sequence[i]][sequence[i+1]]
    return Tcost


def Simulated_Annealing(distances, sequence,T0,Kmax):
    """Returns the best picking sequence"""
    for counter in range(Kmax):
        previous_cost=Total_cost_of(sequence,distances)
        New_sequence = Random_Permutation(sequence)  #Generate a neighbor
        
        current_cost = Total_cost_of(New_sequence, distances)

        if current_cost < previous_cost:
            sequence = New_sequence
            previous_cost = current_cost
        else:
            r = random.uniform(0, 1)
            prob = probability(current_cost, previous_cost, T) #Probability of accepting the neighbor

            if prob >= r: #If not keeps last sequence
                sequence = New_sequence
                previous_cost = current_cost

        T=temperature(TO, counter) #Reduces temperature
        
    
    return sequence #Best picking sequence


def main():
    #it=input("Insert number of random initializations")
    #In case we want to run it with random initializations
    with open('Distance_matrix.csv') as csvfile:
        rows = csv.reader(csvfile)
        Distance_matrix = list(zip(*rows))
    #Distance matrix is now a list of tuples

    order = read_file("orders.txt", int(input("Insert order number : ")))
    print(order)
    
    Kmax = 10000 #Maximum number of iterations
    Temp0 = 10 #INITIAL TEMPERATURE
    Simulated_Annealing(Distance_matrix,order,Temp0,Kmax)
    print(Distance_matrix)
    print("This is the main")
    print("The sequence is:")
    print("The cost is: ")


if __name__ == '__main__':
    main()
#REVISAR PROBABILIDAD DE ACEPTAR UN VECINO MALO