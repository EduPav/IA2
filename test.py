
def read_file(filename, order_number):
    """
    Read "filename" file to return the "order_number"º products list
    filename: string->Name of the file to read
    order_number: int->Number of order to read from the file.
    """
    tmp = []
    if order_number >= 0 and order_number <= 100:
        with open(filename, 'r') as f:
            for line in f:
                tmp.append(line.strip())


    return tmp


tmp=read_file("orders.txt",3)
print(tmp)