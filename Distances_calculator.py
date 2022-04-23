import csv
from a_star import A_Star

# Could be improved to calculate a triangular matrix, but for simplicity and as its not taking long it calculates all


def coord(prod_num, maze):  
    """
    Return coordinates(tuple->row,column) in maze of a specified product
    prod_num: Int->Product number to search for
    maze: List of lists-> Maze with zeros for possible paths and ints!=0 representing products.  
    """
    long_list = []
    for elem in maze:
        for value in elem:
            long_list.append(value)
    c_coord = long_list.index(prod_num) % 13   
    r_coord = int(long_list.index(prod_num)/13)  #Truncates int value
    return r_coord, c_coord


def maze_designer():  # We Need at least 13 blocks of 8 products so we have 104>99. We choose 4x4=128 products design
    """
    Return maze: List of lists-> Maze with zeros for possible paths and ints!=0 representing products. 
    Build it like a 4x4 group of blocks with a size of 4x2 of single width between them.
    """
    maze = []
    for i in range(4*5+1):
        maze.append([])
        for j in range(4*3+1):
            maze[i].append(0)
    prod_num = 1
    for j in range(4):  # Number of block columns
        for i in range(4):  # Number of block rows
            for k in range(4):  # Rows per block
                maze[1+5*i+k][1+3*j] = prod_num
                prod_num += 1
                maze[1+5*i+k][1+3*j+1] = prod_num
                prod_num += 1
    return maze


def closest_valid_position(prod_num, pos): 
    """
    Return the closest valid position (tuple->row,column) to pick up a product
    prod_num: Int->Product number to search for 
    pos: tuple (row,coord)->Product coordinates
    """
    r_coord, c_coord = pos
    if prod_num%2 == 0:
        c_coord += 1    #Even products are picked up from their right
    else:
        c_coord -= 1    #Odd products are picked up from their left
    return r_coord, c_coord



def main():
    """
    Design of the shortest distances matrix between each pair of products.
    Write output to "Distance_matrix.csv" archive
    """
    maze = maze_designer()

    nprod = 99  # Number of products (according to orders archive)
    distance_matrix = []
    for i in range(nprod):  # Complexity n^2 being n the number of products in the facility
        distance_matrix.append([])  #This line adds a row.
        # i references product number i+1
        for j in range(nprod):
            #j references product number j+1
            if i==j: #No need to run A_Star to get distance of a product to itself
                distance_matrix[i].append(1)
                continue
            coord_pickup_a=closest_valid_position(i+1,coord(i+1, maze)) #a is product i+1
            coord_pickup_b=closest_valid_position(j+1,coord(j+1, maze)) #b is product j+1
            ab_path_len = len(A_Star(maze, coord_pickup_a, coord_pickup_b))
            distance_matrix[i].append(ab_path_len) #Add one distance to current row

    #Write distance_matrix list of lists to the archive
    with open("distance_matrix.csv", "w", newline='') as f:
        wr = csv.writer(f)
        wr.writerows(distance_matrix)


if __name__ == '__main__':
    main()
