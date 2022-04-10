
#Determine start and end by input-Klara
#Check if not visiting all the nodes-Edu
#Don't allow the user to select a barrier-Klara
#Comment functions with """ """ -Edu
#Optimize draw-Agus

import pygame   #For a graphic representation
pygame.init()   

GREY = (128, 128, 128)  #Colors hex
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
TURQUOISE = (64, 224, 208)
ORANGE= (255, 165, 0)

Win = pygame.display.set_mode((370, 600))   #Here we set the display 10x16 (depending on draw_layout function square sizes)
pygame.display.set_caption("A STAR algorithm, Exercise 1") #Caption for the display

class Node:
    def __init__(self, parent = None, position = None):
        self.parent = parent
        self.position = position
        self.h = 0
        self.g = 0
        self.f = 0
    def __eq__(self, other):
        return self.position == other.position


def heuristic(cell1, cell2):  #We will use the Manhattan distance
    """Manhattan distance"""
    x1, y1 = cell1
    x2, y2 = cell2

    return abs(x2-x1) + abs (y2-y1)

def A_Star(maze, start, end):
    """You must not select a barrier"""

    start_node = Node(None, start)
    start_node.h = heuristic(start, end)
    start_node.g = 0
    start_node.f = start_node.h + start_node.g

    end_node.h = 0

    #Open and close list
    open_list = [] #An array that contains the nodes that have been generated but have not been examined yet.
    close_list = [] #An array which contains the nodes examined.

    open_list.append(start_node)  #Add the start node

    #Loop
    while len(open_list) > 0:
        current_node = open_list[0]
        current_index = 0

        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index
        
        #Pop eliminates the current node from the open list and then with append we add it to the close list
        open_list.pop(current_index)
        close_list.append(current_node)


        #Goal
        if current_node == end_node:
            path = []  #List with the path
            while current_node is not None: #It goes from last node to the start one going through parent nodes.
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]

        # Generate Leaves
        leaves = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            #Get neighbour node position
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            #Within range
            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[0]) -1) or node_position[1] < 0:
                continue
            #Make sure we are not in a barrier
            if maze[node_position[0]][node_position[1]] != 0:
                continue
            new_node = Node(current_node, node_position)
            inCloseList=False
            #for leave in leaves:
            for closed_leave in close_list:
                if new_node==closed_leave:
                    inCloseList=True
                        
            if inCloseList:
                continue
            #New node
            

            leaves.append(new_node)

        #Loop for leaves
        for leave in leaves:
        
            #Heuristic, g() and f() values
            leave.g = current_node.g + 1
            leave.h = heuristic(leave.position, end_node.position)
            leave.f = leave.g + leave.h

            #Leave already in open list
            inOpenList=False
            for open_node in open_list:
                if leave == open_node:
                    inOpenList=True
            if inOpenList:
                continue
            open_list.append(leave)



def draw_grid(win, rows, width):
    GAP = width//rows
    for i in range(rows):
        pygame.draw.line(win, GREY, (0 , i*GAP), (width , i*GAP))  #Here we draw the horizontal lines 
        for j in range(rows):
            pygame.draw.line(win, GREY, (j*GAP , 0), (j*GAP , width))  #Here we draw the vertical lines

def draw(win, x, y, width, color):
        pygame.draw.rect(win, color, (x, y, width, width))



def draw_Start_End(start, end):
    draw(Win, start[1]*37.5, start[0]*37.5, 37.5, TURQUOISE)
    draw(Win, end[1]*37, end[0]*37, 37.5, ORANGE)

def draw_maze(x, y):
    draw(Win, x*37, y*37, 37.5, BLACK)

def draw_path(path):
    for x in range (len(path)):
        if x > 0 and x < len(path)-1:
            y, x = path[x]
            draw(Win, x*37, y*37, 37.5, GREEN)



def input_coordinates(maze, position = None):
    values = []
    if(position == "end"):
        string = "Enter the coordinate for end node :"
    elif(position == "start"):
        string = "Enter the coordinates for start node :"
    else:
        string = "Enter the coordinates of "
    print(string)
    for coord in ('x : ', 'y : '):
        values.append(int(input(coord)))
    print("\n")
    
        
    for i in values:
        if i != None and maze[values[0]][values[1]] == 0:
            return values
        else:
            print("You typed something wrong !")
            return 0



def main():
    maze = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 1, 0, 1, 1, 0, 1, 1, 0],
            [0, 1, 1, 0, 1, 1, 0, 1, 1, 0],
            [0, 1, 1, 0, 1, 1, 0, 1, 1, 0],
            [0, 1, 1, 0, 1, 1, 0, 1, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 1, 0, 1, 1, 0, 1, 1, 0],
            [0, 1, 1, 0, 1, 1, 0, 1, 1, 0],
            [0, 1, 1, 0, 1, 1, 0, 1, 1, 0],
            [0, 1, 1, 0, 1, 1, 0, 1, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 1, 0, 1, 1, 0, 1, 1, 0],
            [0, 1, 1, 0, 1, 1, 0, 1, 1, 0],
            [0, 1, 1, 0, 1, 1, 0, 1, 1, 0],
            [0, 1, 1, 0, 1, 1, 0, 1, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    
    
    start_position = 0
    end_position = 0
    
    while start_position == 0:
        start_position = input_coordinates(maze, "start")
    while end_position == 0:
        end_position = input_coordinates(maze, "end")
    

    start = (start_position[0], start_position[1])   #(FILAS, COLUMNAS)
    end = (end_position[0], end_position[1])

    path = A_Star(maze, start, end)
    print(path)
    y = len(maze[0])
    x = len(maze)
    f = len(path)
    
    for i in range(f):
        if i < len(path)-1:
            x, y = path[i]
            maze[x][y]=2
        else:
            x, y = path[i]
            maze[x][y]=3
    
    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
      for row in maze]))  #Print the matrix

    
    pygame.draw.rect(Win, WHITE, (0, 0, 600, 600))
    draw_grid(Win, 16, 600)
    k=1
    
    draw_Start_End(start, end)
    draw_path(path)
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 1:
                draw_maze(j, i)
    while k>0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        pygame.display.update()  #Function of pygame that updates the display

if __name__ == '__main__':
    main()



    
