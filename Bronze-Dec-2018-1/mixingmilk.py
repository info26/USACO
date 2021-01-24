# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 19:14:09 2019

@author: study
"""

#No comments this time! 
f = open("mixmilk.in","r")
state = 1
b1 = list(map(int, f.readline().split(" ")))
b2 = list(map(int, f.readline().split(" ")))
b3 = list(map(int, f.readline().split(" ")))
f.close()
for i in range(100):
    if state == 1:
        if b1[1] + b2[1] > b2[0]:
            b1[1] = (b1[1] + b2[1]) - b2[0]
            b2[1] = b2[0]
        else:
            
            b2[1] = b1[1] + b2[1]
            b1[1] = 0
        if state == 3:
            state = 1
        else: 
            state = state + 1
        continue
    if state == 2:
        if b2[1] + b3[1] > b3[0]:
            b2[1] = (b2[1] + b3[1]) - b3[0]
            b3[1] = b3[0]
        else:
            b3[1] = b2[1] + b3[1]
            b2[1] = 0
        if state == 3:
            state = 1
        else: 
            state = state + 1
        continue
    if state == 3:
        
        if b3[1] + b1[1] > b1[0]:
            b3[1] = (b3[1] + b1[1]) - b1[0]
            b1[1] = b1[0]
        else:
            b1[1] = b3[1] + b1[1]
            b3[1] = 0
        if state == 3:
            state = 1
        else: 
            state = state + 1
        continue
f = open("mixmilk.out","w")
f.write(str(b1[1])+"\n"+str(b2[1])+"\n"+str(b3[1])+"\n")
f.close()