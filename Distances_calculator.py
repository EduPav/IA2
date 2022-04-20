import csv
from a_star import A_Star
#Funcion que devuelve la coordenada, dado un numero de producto.  coord()
#Entra maze
#Could be improved to calculate a triangular matrix, but for simplicity and as its not taking long calculates all

def coord(producto): #Change by oficial coordinates function
    coordenada=(0,0)
    return coordenada

maze=[[0,0,0,0,0,0,0],
      [0,1,2,0,3,4,0],
      [0,5,6,0,7,8,0],
      [0,0,0,0,0,0,0]]

nprod=99 #Number of products
Distance_matrix=[]
for i in range(nprod):  #Complexity n^2 being n the number of products in the facilitiy
    Distance_matrix.append([]) #It becomes a list of lists
    #i references product number i+1
    for j in range(nprod):
        ABpathLen=len(A_Star(maze,coord(i),coord(j)))
        Distance_matrix[i].append(ABpathLen)
    

with open("Distance_matrix.csv", "w",newline='') as f:
    wr = csv.writer(f)
    wr.writerows(Distance_matrix)

