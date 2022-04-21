import csv
from a_star import A_Star
# Funcion que devuelve la coordenada, dado un numero de producto.  coord()
# Entra maze
# Could be improved to calculate a triangular matrix, but for simplicity and as its not taking long calculates all


def coord(prod_num, maze):  # Change by oficial coordinates function
    long_list = []
    for elem in maze:
        for value in elem:
            long_list.append(value)
    c_coord = long_list.index(prod_num) % 13
    r_coord = int(long_list.index(prod_num)/13)  # Truncates int value
    return r_coord, c_coord


def maze_designer():  # Need 13 blocks. of 8 so we have 104. 4x4=128
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


def closest_valid_position(prod_nb, pos):
    """Returns the closest valid position of a product"""
    r_coord, c_coord = pos
    if prod_nb%2 == 0:
        c_coord += 1
    else:
        c_coord -= 1
    return r_coord, c_coord




maze = maze_designer()

nprod = 99  # Number of products
distance_matrix = []
for i in range(nprod):  # Complexity n^2 being n the number of products in the facilitiy
    distance_matrix.append([])  # It becomes a list of lists
    # i references product number i+1
    for j in range(nprod):
        if i==j:
            distance_matrix[i].append(1)
            continue
        coord_a=closest_valid_position(i+1,coord(i+1, maze))
        coord_b=closest_valid_position(j+1,coord(j+1, maze))
        ABpath_len = len(A_Star(maze, coord_a, coord_b))
        distance_matrix[i].append(ABpath_len)


with open("distance_matrix.csv", "w", newline='') as f:
    wr = csv.writer(f)
    wr.writerows(distance_matrix)
