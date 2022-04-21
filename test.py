from a_star import A_Star

def maze_designer(): #Need 13 blocks. of 8 so we have 104. 4x4=128
    maze=[]
    for i in range(4*5+1):
        maze.append([])
        for j in range(4*3+1):
            maze[i].append(0)
    prod_num=1
    for j in range(4): #Number of block columns
        for i in range(4):#Number of block rows
            for k in range(4): #Rows per block
                maze[1+5*i+k][1+3*j]=prod_num
                prod_num+=1
                maze[1+5*i+k][1+3*j+1]=prod_num
                prod_num+=1
    return maze


def coord(prod_num,maze):
    long_list=[]
    for elem in maze:
        for value in elem:
            long_list.append(value)
    x_coord=long_list.index(prod_num)%13
    y_coord=int(long_list.index(prod_num)/13)
    print(y_coord,x_coord)

maze=maze_designer()
print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
for row in maze]))  #Print the matrix

coord(99,maze)

A_Star(maze,(1,1),(1,2))