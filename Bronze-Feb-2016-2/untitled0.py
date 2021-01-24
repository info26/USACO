# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 20:51:41 2020

@author: study
"""
f = open("cbarn.in", "r")

rooms = []
movlist = []

a = int(f.readline())
for i in range(a):
    rooms.append(int(f.readline()))
f.close()
for a in range(len(rooms)):
    moves = 0
    for b in range(len(rooms)):
        # How far away is this room???
        if b == a:
            # nope. 
            continue
        if b < a:
            # Ok, so the cows will have to loop around the list.
            dist = (b + 1) + (len(rooms) - a - 1)
        else:
            dist = abs(a - b)
        moves += dist*rooms[b]
    movlist.append(moves)
    
    
    
f = open("cbarn.out", "w")
f.write(str(min(movlist)))
f.close()

