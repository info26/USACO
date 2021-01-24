# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 14:29:55 2019

@author: study
"""
f = open("tttt.in","r")
swc = 0
swccs  = set()
dwccs = set()
#no comments either. 
tiles = []
for i in range(3):
    tiles.append(f.readline())
f.close();
#check if anyone can with solo. 
#     Possible winnings
#  1    2    3    4    5    6
# XXX  OOO  OOO  XOO  OOX  XOO
# OOO  XXX  OOO  OXO  OXO  XOO
# OOO  OOO  XXX  OOX  XOO  XOO
#  7    8
# OXO  OOX
# OXO  OOX
# OXO  OOX
for i in tiles:
    if (i[0] == i[1]) == True and (i[0] == i[2]) == True:
        
        if i[0] not in swccs:
            #then this satisfies cases 1-3
            #(see above)
            #then we add one to solowincount
            print("Horizontal!", i[0], i)
            swccs.add(i[0])
        else:
            continue
    #verticals:
for i in range(3):
    if (tiles[0][i] == tiles[1][i]) == True and (tiles[0][i] == tiles[2][i]) == True:
        #this satisfies cases 6-8:
        if tiles[0][i] not in swccs:
            print("Vertical!")
            swccs.add(tiles[0][i])
        else:
            continue
#diagonals.
if (tiles[0][0] == tiles[1][1]) == True and (tiles[0][0] == tiles[2][2]) == True:
    if tiles[0][0] not in swccs:
        print("Diagonal!")
        swccs.add(tiles[0][0])
if (tiles[0][2] == tiles[1][1]) == True and (tiles[2][0] == tiles[0][2]) == True:
    if tiles[0][2] not in swccs:
        print("Diagonal!")
        swccs.add(tiles[0][2])
#next, duos. 
for i in tiles:
    
    temp = {i[0],i[1],i[2]}
    temp = list(temp)
    if len(temp) == 2:
        if (temp[0],temp[1]) not in dwccs:
            dwccs.add((temp[0],temp[1]))
            dwccs.add((temp[1],temp[0]))
    #verticals:
for i in range(3):
    temp = {tiles[0][i], tiles[1][i], tiles[2][i]}
    temp = list(temp)
    if len(temp) == 2:
        if (temp[0],temp[1]) not in dwccs:
            dwccs.add((temp[0],temp[1]))
            dwccs.add((temp[1],temp[0]))
#diagonals.
temp = {tiles[0][0],tiles[1][1],tiles[2][2]}
temp = list(temp)
if len(temp) == 2:
    if (temp[0],temp[1]) not in dwccs:
        dwccs.add((temp[0],temp[1]))
        dwccs.add((temp[1],temp[0]))
temp = {tiles[0][2],tiles[1][1],tiles[2][0]}
temp = list(temp)
if len(temp) == 2:
    if (temp[0],temp[1]) not in dwccs:
        dwccs.add((temp[0],temp[1]))
        dwccs.add((temp[1],temp[0]))
f = open("tttt.out","w")
f.write(str(len(swccs)) + "\n")
f.write(str(int(len(dwccs)/2)) + "\n")
f.close()