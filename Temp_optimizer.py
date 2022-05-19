import matplotlib.pyplot as plt
from Simulated_Annealing import simulated_annealing
import csv
import statistics as st

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
    #Read external archive
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
    num_orders = len(orders)
    print(str(num_orders)+" orders will be analyzed")

    #Simulated annealing parameters testing
    Kmax = 1000 #Maximum number of iterations
    num_runs=100
    orders_computed=0
    
    #100Simulated/orden*1000it/Simulated*10orden/Temp*8Temp= 8 Millones it
    tot_cost_list=[]
    avg_stdev_list=[]
    Temp_list=[2.5,15,20,25,30,35,250,2500]
    for Temp0 in Temp_list:
        total_cost_for_temp=0
        stdevtot=0
        for order in orders:
            avg_cost=0
            costs_along_runs=[]
            for _ in range(num_runs):
                _,_,_,best_cost=simulated_annealing(distance_matrix,order,Temp0,Kmax)
                avg_cost+=best_cost
                costs_along_runs.append(best_cost)
            avg_cost/=num_runs
            #print("Its cost is: "+str(avg_cost))
            #Calculate avg and standard deviation of best costs
            stdev=st.stdev(costs_along_runs)
            #avg=st.mean(costs_along_runs)
            #print("95% of best costs fall between +-"+str(2*stdev))
            #print("avg="+str(avg))
            #
            total_cost_for_temp+=avg_cost
            orders_computed+=1
            print(str(orders_computed)+" orders have been optimized")
            stdevtot+=stdev
        stdev_avg=stdevtot/len(orders)
        print("For Temp0="+str(Temp0)+" the total cost is "+str(total_cost_for_temp))
        print("The stdev average for the orders is "+str(stdev_avg))
        tot_cost_list.append(total_cost_for_temp)
        avg_stdev_list.append(stdev_avg)
    print("Used temps="+str(Temp_list))
    print("Costs:"+str(tot_cost_list))
    print("stdev_avg: "+str(avg_stdev_list))
    plt.plot(Temp_list,tot_cost_list)
    plt.title("Final cost vs Temperature")
    plt.xlabel('Temperature')
    plt.ylabel('Cost of ' + str(num_orders) + 'orders')
    plt.show()
    plt.plot(Temp_list,avg_stdev_list)
    plt.title("Standard deviations with each temperature")
    plt.xlabel('Temperature')
    plt.ylabel('Standard deviations')
    plt.show()



if __name__=='__main__':
    main()