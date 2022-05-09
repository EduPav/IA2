import matplotlib.pyplot as plt

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

orders=[]
for i in range(100):
    order = read_file("orders.txt", i+1)
    for product in order:
        orders.append(product)

plt.hist(orders, bins =100)

plt.show()


