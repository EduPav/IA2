import matplotlib.pyplot as plt
from simulated_annealing import simulated_annealing
import csv

#Get standard deviation also? So its not only avg plotting
#maybe you get more random values with certain temperatures. Avg is not helping to decide

def read_file(file_name, order_number):
    """
    Read "filename" file to return the "order_number"º products list
    filename: string->Name of the file to read
    order_number: int->Number of order to read from the file.
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

def orders_length(file_name):
    lengths=[]
    for i in range(100):
        order=read_file(file_name,i+1)
        lengths.append(len(order))
    return lengths




def main():
    ##Orders lengths distribution
    #lengths=orders_length("orders.txt")
    #plt.hist(lengths,4)
    #plt.show()
    ##Resulting groups: <15; 15-19; 20-23; 24<

    #Read external archives
    with open('distance_matrix.csv') as csvfile:
        rows = csv.reader(csvfile)
        distance_matrix = list(zip(*rows))
    
    
    #Filter orders per length
    case=input("choose lengths to analize for optimal temp\n1:<15\n2:15-19\n3:20-23\n4:23<\nYour pick: ")
    orders=[]
    for i in range(100):
        order = read_file("orders.txt", i+1)
        case1=(case=='1' and len(order)<15)
        case2=(case=='2' and len(order)>=15 and len(order)<=19)
        case3=(case=='3' and len(order)>=20 and len(order)<=23)
        case4=(case=='4' and len(order)>23)
        if case1 or case2 or case3 or case4:
            orders.append(order)
    #orders has all every single order in orders.txt with the length range determined by user
    print(str(len(orders))+" orders will be analyzed")
    #Simulated annealing parameters testing
    Kmax = 10000 #Maximum number of iterations
    Temp0 = 0.1 #INITIAL TEMPERATURE 
    #10000 Kmax, 10 runs
    #1->2741,2731
    #10->2758
    #100->2746
    #1000->2746
    #10000->2730
    num_runs=10
    total_cost_for_temp=0
    orders_computed=0
    for order in orders:
        avg_cost=0
        #costs_list_avg=[0]*Kmax
        for _ in range(num_runs):
            _,_,_,best_cost=simulated_annealing(distance_matrix,order,Temp0,Kmax)
            #costs_list_avg= [i+j for i,j in zip(costs_list_avg,costs_evolution)]
            avg_cost+=best_cost
        avg_cost/=num_runs
        #costs_list_avg=[i/num_runs for i in costs_list_avg]
        print("Its cost is: "+str(avg_cost))
        #plt.plot(costs_list_avg)
        #plt.show()
        total_cost_for_temp+=avg_cost
        orders_computed+=1
        print(str(orders_computed)+" orders have been optimized")
    print("For Temp0="+str(Temp0)+" the total cost is "+str(total_cost_for_temp))



if __name__=='__main__':
    main()