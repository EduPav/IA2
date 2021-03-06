from Simulated_Annealing import simulated_annealing
import matplotlib.pyplot as plt
import csv


def plot_costs(costs_list):
    """  Plots the costs list vs its place in the list

    Args:
        costs_list (list): Cost values
    """
    plt.plot(costs_list, color='magenta', marker='o' ) #plot the data

    plt.ylabel('costs') #set the label for y axis
    plt.xlabel('iteration') #set the label for x-axis
    plt.title("Simulated annealing costs along iterations") #set the title of the graph
    plt.show() #display the graph

def plot_probs(probs_list):
    """Plots the probs list vs its place in the list

    Args:
        probs_list (list): probability values
    """
    plt.plot(probs_list, color='magenta', marker='o' ) #plot the data

    plt.ylabel('Probability') #set the label for y axis
    plt.xlabel('Iteration') #set the label for x-axis
    plt.title("Simulated annealing probs along iterations") #set the title of the graph
    plt.show() #display the graph

def read_file(file_name, order_number):
    """
    Returns an order in the file
    Args:
        file_name (string): Name of the file to read
        order_number (int): Number of order to read from the file.

    Returns:
        _list_: "order_number"º products list in "filename" file 
    """
    result = []
    tmp = []
    if order_number >= 0 and order_number <= 100:
        command = "Order " + str(order_number)
        with open(file_name, 'r') as f:
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
    #it=input("Insert number of random initializations")
    #In case we want to run it with random initializations
    with open('TP1/Exercise_2/distance_matrix.csv') as csvfile:
        rows = csv.reader(csvfile)
        distance_matrix = list(zip(*rows))
    #Distance matrix is now a list of tuples of STRINGS

    #order = read_file("orders.txt", int(input("Insert order number : ")))
    order = read_file("TP1/Exercise_2/orders.txt", 9)
    print("Order to analize: "+str(order))
    
    Kmax = 1000 #Maximum number of iterations
    Temp0 = 25 #INITIAL TEMPERATURE
    probs,costs_evolution,best_sequence,best_cost=simulated_annealing(distance_matrix,order,Temp0,Kmax)
    print("The best sequence found is:"+str(best_sequence))
    print("Its cost is: "+str(best_cost))
    plot_costs(costs_evolution)
    plot_probs(probs)
    
if __name__ == '__main__':
    main()

