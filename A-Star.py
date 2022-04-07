
import pygame
pygame.init()

GREY = (128, 128, 128)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
TURQUOISE = (64, 224, 208)
ORANGE= (255, 165, 0)

Win = pygame.display.set_mode((370, 600))   #Here we set the display 10x16
pygame.display.set_caption("A STAR algorithm, Exercise 1") #Caption for the display

class Node:
    def __init__(self, parent = None, position = None):
        self.parent = parent
        self.position = position
        self.heuristic_Cost = 0
        self.g_cost = 0
        self.f_cost = 0
    def __eq__(self, other):
        return self.position == other.position


def heuristic(cell1, cell2):  #We will use the Manhattan distance
    x1, y1 = cell1
    x2, y2 = cell2

    return abs(x2-x1) + abs (y2-y1)

def g():  #This si the cost
    x = 1
    return x

def A_Star(maze, start, end):
    """You might not select a barrier"""
    #rowS, colS = start
    
    start_node = Node(None, start)
    start_node.heuristic_Cost = heuristic(start, end)
    start_node.g_cost = 0
    start_node.f_cost = start_node.heuristic_Cost + start_node.g_cost

    #rowE, colE = end
    end_node = Node(None, end) 
    end_node.heuristic_Cost = 0

    #Open and close list
    open_list = [] #An array that contains the nodes that have been generated but have not been yet examined till yet.
    close_list = [] #An array which contains the nodes which are examined.

    open_list.append(start_node)  #Add the start node

    #Loop
    while len(open_list) > 0:
        current_node = open_list[0]
        current_index = 0

        for index, item in enumerate(open_list):           #REVISAR
            if item.f_cost < current_node.f_cost:
                current_node = item
                current_index = index
        
        #Pop eliminates the current node from the open list and then with append we add it to the close list
        open_list.pop(current_index)
        close_list.append(current_node)


        #Goal
        if current_node == end_node:
            path = []  #List with the path
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1] #Reversed path

        # Generate Leaves
        leaves = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            #Get node position
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            #Within range
            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) -1) or node_position[1] < 0:
                continue
            #Make sure we are not in a barrier
            if maze[node_position[0]][node_position[1]] != 0:
                continue

            #New node
            new_node = Node(current_node, node_position)

            leaves.append(new_node)

        #Loop for leaves
        for leave in leaves:
            for closed_leave in close_list:
                if leave == closed_leave:
                    continue
        
            #Heuristic, g() and f() values
            leave.g_cost = current_node.g_cost + 1
            leave.heuristic_Cost = heuristic(leave.position, end_node.position)
            leave.f_cost = leave.g_cost + leave.heuristic_Cost

            #Leave already in open list
            for open_node in open_list:
                if leave == open_node and leave.g_cost > open_node.g_cost:
                    continue

            #ADD LEAVE TO THE OPEN LIST
            open_list.append(leave)


def draw_grid(win, rows, width):
    GAP = width//rows
    for i in range(rows):
        pygame.draw.line(win, GREY, (0 , i*GAP), (width , i*GAP))  #Here we draw the horizontal lines 
        for j in range(rows):
            pygame.draw.line(win, GREY, (j*GAP , 0), (j*GAP , width))  #Here we draw the vertical lines

def draw(win, x, y, width, color):
        pygame.draw.rect(win, color, (x, y, width, width))

def draw_Gondolas():
    draw(Win, 37.5, 37.5, 37.5, BLACK )
    draw(Win, 37.5, 75, 37.5, BLACK )
    draw(Win, 37.5, 112.5, 37.5, BLACK )
    draw(Win, 37.5, 149, 37.5, BLACK )
    draw(Win, 75, 37.5, 37.5, BLACK )
    draw(Win, 75, 75, 37.5, BLACK )
    draw(Win, 75, 112.5, 37.5, BLACK )
    draw(Win, 75, 149, 37.5, BLACK )

    draw(Win, 186.5, 37.5, 37.5, BLACK )
    draw(Win, 186.5, 75, 37.5, BLACK )
    draw(Win, 186.5, 112.5, 37.5, BLACK )
    draw(Win, 186.5, 149, 37.5, BLACK )
    draw(Win, 149, 37.5, 37.5, BLACK )
    draw(Win, 149, 75, 37.5, BLACK )
    draw(Win, 149, 112.5, 37.5, BLACK )
    draw(Win, 149, 149, 37.5, BLACK )

    draw(Win, 260.5, 37.5, 37.5, BLACK )
    draw(Win, 260.5, 75, 37.5, BLACK )
    draw(Win, 260.5, 112.5, 37.5, BLACK )
    draw(Win, 260.5, 149, 37.5, BLACK )
    draw(Win, 297, 37.5, 37.5, BLACK )
    draw(Win, 297, 75, 37.5, BLACK )
    draw(Win, 297, 112.5, 37.5, BLACK )
    draw(Win, 297, 149, 37.5, BLACK )

    draw(Win, 149, 223, 37.5, BLACK )
    draw(Win, 149, 260.5, 37.5, BLACK )
    draw(Win, 149, 297, 37.5, BLACK )
    draw(Win, 149, 334.5, 37.5, BLACK )
    draw(Win, 186.5, 223, 37.5, BLACK )
    draw(Win, 186.5, 260.5, 37.5, BLACK )
    draw(Win, 186.5, 297, 37.5, BLACK )
    draw(Win, 186.5, 334.5, 37.5, BLACK )

    draw(Win, 37.5, 223, 37.5, BLACK )
    draw(Win, 37.5, 260.5, 37.5, BLACK )
    draw(Win, 37.5, 297, 37.5, BLACK )
    draw(Win, 37.5, 334.5, 37.5, BLACK )
    draw(Win, 75, 223, 37.5, BLACK )
    draw(Win, 75, 260.5, 37.5, BLACK )
    draw(Win, 75, 297, 37.5, BLACK )
    draw(Win, 75, 334.5, 37.5, BLACK )

    draw(Win, 260.5, 223, 37.5, BLACK )
    draw(Win, 260.5, 260.5, 37.5, BLACK )
    draw(Win, 260.5, 297, 37.5, BLACK )
    draw(Win, 260.5, 334.5, 37.5, BLACK )
    draw(Win, 297, 223, 37.5, BLACK )
    draw(Win, 297, 260.5, 37.5, BLACK )
    draw(Win, 297, 297, 37.5, BLACK )
    draw(Win, 297, 334.5, 37.5, BLACK )

    draw(Win, 37.5, 407.5, 37.5, BLACK )
    draw(Win, 37.5, 445, 37.5, BLACK )
    draw(Win, 37.5, 482.5, 37.5, BLACK )
    draw(Win, 37.5, 519, 37.5, BLACK )
    draw(Win, 75, 407.5, 37.5, BLACK )
    draw(Win, 75, 445, 37.5, BLACK )
    draw(Win, 75, 482.5, 37.5, BLACK )
    draw(Win, 75, 519, 37.5, BLACK )

    draw(Win, 149, 407.5, 37.5, BLACK )
    draw(Win, 149, 445, 37.5, BLACK )
    draw(Win, 149, 482.5, 37.5, BLACK )
    draw(Win, 149, 519, 37.5, BLACK )
    draw(Win, 186.5, 407.5, 37.5, BLACK )
    draw(Win, 186.5, 445, 37.5, BLACK )
    draw(Win, 186.5, 482.5, 37.5, BLACK )
    draw(Win, 186.5, 519, 37.5, BLACK )

    draw(Win, 260.5, 407.5, 37.5, BLACK )
    draw(Win, 260.5, 445, 37.5, BLACK )
    draw(Win, 260.5, 482.5, 37.5, BLACK )
    draw(Win, 260.5, 519, 37.5, BLACK )
    draw(Win, 297, 407.5, 37.5, BLACK )
    draw(Win, 297, 445, 37.5, BLACK )
    draw(Win, 297, 482.5, 37.5, BLACK )
    draw(Win, 297, 519, 37.5, BLACK )

def draw_Start_End(start, end):
    draw(Win, start[1]*37.5, start[0]*37.5, 37.5, TURQUOISE)
    draw(Win, end[1]*37, end[0]*37, 37.5, ORANGE)


def draw_path(path):
    for x in range (len(path)):
        if x > 0 and x < len(path)-1:
            y, x = path[x]
            draw(Win, x*37, y*37, 37.5, GREEN)

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

    start = (0, 0)   #(FILAS, COLUMNAS)
    end = (3, 6)

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
    draw_Gondolas()
    draw_Start_End(start, end)
    draw_path(path)
    while k>0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
    #pygame.draw.rect(Win, WHITE, (50, 50, 600, 600))
        pygame.display.update()  #Function of pygame that updates the display

if __name__ == '__main__':
    main()

#LO QUE SE PUEDE AGREGAR ES QUE SE ELIJA EL PRINCIPIO Y EL FINAL CON EL MOUSE

    
