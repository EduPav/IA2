import pygame   #For a graphic representation
pygame.init()   

GREY = (128, 128, 128)  #Colors hex code
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


def heuristic(cell1, cell2):  
    """Returns manhattan distance"""
    x1, y1 = cell1
    x2, y2 = cell2

    return abs(x2-x1) + abs (y2-y1)

def A_Star(maze, start, end):
    """Returns shortest path from start to end"""

    start_node = Node(None, start)
    start_node.h = heuristic(start, end)
    start_node.g = 0
    start_node.f = start_node.h + start_node.g

    end_node = Node(None, end)
    end_node.h = 0

    #Open and close list
    open_list = [] #An array that contains the nodes that have been generated but have not been expanded yet.
    close_list = [] #An array which contains the expanded nodes.

    open_list.append(start_node)  

    #Loop
    while len(open_list) > 0:
        current_node = open_list[0] #Not necessarily an ordered list
        current_index = 0

        for index, item in enumerate(open_list): #n complexity
            if item.f < current_node.f:
                current_node = item #Node class
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
            neighbour_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            #Guarantees neighbours inside the warehouse
            if neighbour_position[0] > (len(maze) - 1) or neighbour_position[0] < 0 or neighbour_position[1] > (len(maze[0]) -1) or neighbour_position[1] < 0:
                continue
            #Guarantees we are not in a barrier
            if maze[neighbour_position[0]][neighbour_position[1]] != 0:
                continue
            new_node = Node(current_node, neighbour_position)
            inCloseList=False
            #for leave in leaves:
            for closed_leave in close_list:#n complexity
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
            for open_node in open_list: #n complexity
                if leave == open_node:
                    inOpenList=True
            if inOpenList:
                continue
            open_list.append(leave)


def input_coordinates(maze, position = None):
    """Asks for valid coordinates to user and returns them"""
    #Reads coordinates
    values = []
    if(position == "end"):
        print("Enter the coordinate for end node :")
    elif(position == "start"):
        print("Enter the coordinates for start node :")

    for coord in ('y : ', 'x : '):
        values.append(int(input(coord)))
    print("\n")
    
    #Checks coordinates
    if values[0]<0 or values[1]<0 or values[0]>=len(maze) or values[1]>=len(maze[0]):
        print("Coordinates outside the warehouse")
        return 0
    if values[0] != None and values[1]!=None and maze[values[0]][values[1]] == 0:
        return values
    else:
        print("You can't select a barrier")
        return 0



def draw_grid(win, rows, width):
    GAP = width//rows
    for i in range(rows):
        pygame.draw.line(win, GREY, (0 , i*GAP), (width , i*GAP))  #Here we draw the horizontal lines 
        for j in range(rows):
            pygame.draw.line(win, GREY, (j*GAP , 0), (j*GAP , width))  #Here we draw the vertical lines

def draw(win, x, y, width, color):
    """Paints a square"""
    pygame.draw.rect(win, color, (x, y, width, width))



def draw_Start_End(start, end):
    """Paints squares in start and end positions"""
    draw(Win, start[1]*37.5, start[0]*37.5, 37.5, TURQUOISE)
    draw(Win, end[1]*37, end[0]*37, 37.5, ORANGE)

def draw_maze(x, y):
    """Paints a barrier"""
    draw(Win, x*37, y*37, 37.5, BLACK)

def draw_path(path):
    """Paints list of coordinates"""
    for x in range (len(path)):
        if x > 0 and x < len(path)-1:
            y, x = path[x]
            draw(Win, x*37, y*37, 37.5, GREEN)



if __name__ == '__main__':

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
    

    start = (start_position[0], start_position[1])   #(ROW,COLUMN)//(Y,X)
    end = (end_position[0], end_position[1])

    path = A_Star(maze, start, end)
    print(path)
    y = len(maze[0])
    x = len(maze)
    f = len(path)
    print("The shortest path has a length of "+str(f))
    
#In case we want to print the matrix instead of the visual representation with pygame   
#    for i in range(f):
#        if i < len(path)-1:
#            x, y = path[i]
#            maze[x][y]=2
#        else:
#            x, y = path[i]
#            maze[x][y]=3
#

#    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
#      for row in maze]))  #Print the matrix

    
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





    
