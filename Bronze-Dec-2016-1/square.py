# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 14:59:15 2019

@author: study
"""
f = open("square.in","r")

ans = 0
r1 = list(map(int, f.readline().split(" ")))
r2 = list(map(int, f.readline().split(" ")))
f.close()
#Calculate the x distance between the right-most point from b1
#o the left most point on b2. ABS is needed. 
xdis = abs(r1[2] - r2[0])
xdis3 = abs(r2[2] - r1[0])
xdis1 = abs(r1[2] - r1[0])
xdis2 = abs(r2[2] - r2[0])
ydis = abs(r1[3] - r2[1])
ydis3 = abs(r2[3] - r1[1])
ydis1 = abs(r1[3] - r1[1])
ydis2 = abs(r2[3] - r2[1])
temp = max(xdis,ydis,xdis1,xdis2,ydis1,ydis2,xdis3,ydis3)
f = open("square.out","w")
f.write(str(temp ** 2) + "\n")
f.close()