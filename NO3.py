import os
import sys
import csv
from math import sqrt, cos, radians

#this function creates 2 lists with the N and O coordinates and it will be applied to the two separete blocks 
def sep_N_O(block):
    block_N = []
    block_O = [] 
    block_K = []
    for i in range(0, len(block)-1):
        if block[i].split()[0] =="N":
            block_N.append(block[i+1])
    for i in range(0, len(block)-1):
        if block[i].split()[0] =="O":
            block_O.append(block[i+1])
    for i in range(0, len(block)-1):
        if block[i].split()[0] =="K":
            block_K.append(block[i])
            block_K.append(block[i+1])
    return block_N, block_O , block_K 

#this function calculates the distance between the points P1 and P2 included in the lists 
def distance(P1, P2):
    P1=P1.split()
    P2=P2.split()
    P1 = [float(x) for x in P1]
    P2 = [float(x) for x in P2]
    d2 = ((P2[0]-P1[0])**2 + (P2[1]-P1[1])**2 + (P2[2]-P1[2])**2)
    d = d2**(1/2)
    return d

def conversion(block,cart_to_frac,fract_to_cart):
    cell_x = float(str(lines[2]).split()[0])
    cell_y = float(str(lines[3]).split()[1])
    cell_z = float(str(lines[4]).split()[2])
    if cart_to_frac==1:
        for i in range(len(block)):
            x = float(block[i].split()[0])
            x = str(x/cell_x)
            y = float(block[i].split()[1])
            y = str(y/cell_y)
            z = float(block[i].split()[2])
            z = str(z/cell_z)
            block[i]= x + " " + y + " " + z
        return(block)
    if fract_to_cart == 1:
        for i in range(len(block)):
            x = float(block[i].split()[0])
            x = str(x*cell_x)
            y = float(block[i].split()[1])
            y = str(y*cell_y)
            z = float(block[i].split()[2])
            z = str(z*cell_z)
            block[i]= x + " " + y + " " + z    
            
        return(block)



folder =  os.path.dirname(os.path.realpath(__file__))
config = open(folder + '/07_12.cfg','r')
config_NO3 = open("CONFIG_NO3.txt", "w", newline = "")

for l in config:
    if l.split()[0] != "N":
        print("K")
        #config_NO3.write(l)
    if l.split()[0] == "N":
        nitro_number = l.split()[1]
        break
print(nitro_number)
config.close()

config = open(folder + '/CONFIG','r')

lines = []

for i in config:
    lines.append(i)


#conversion to fractional coordinates
block_N, block_O,block_K = sep_N_O(lines)
block_N_frac=block_N.copy()
block_O_frac=block_O.copy()
block_N_frac=conversion(block_N_frac,1,0)
block_O_frac=conversion(block_O_frac,1,0)

for line in block_K:
    config_NO3.write(line)

for N, n in enumerate(block_N_frac):
    print(N)
    N_dist = []
    for O, o in enumerate(block_O_frac):
        dist = distance(n,o)
        N_dist.append((O, dist))
    NO3_dist = N_dist.copy()
    NO3_dist.sort(key=lambda x:x[1])
    NO3_dist = [x[0] for x in NO3_dist[0:3]]
    config_NO3.write("N            "+str(N+int(nitro_number))+"\n")
    config_NO3.write(block_N[N])
    for i, x in enumerate(NO3_dist):
        config_NO3.write("O            "+str(NO3_dist[i])+"\n")
        config_NO3.write(block_O[x])
    
    
    
print("FINISHED")
