

f = open("teleport.in", "r")
dat = list(map(int, f.readline().split(" ")))

dist = []

# Using teleporter x => y
dist.append(
    # Distance from start --> x
    abs(dat[0] - dat[2]) +
    # Distance from y --> end
    abs(dat[3] - dat[1]) 
)
# Using teleporter y => x
dist.append(
    # Distance from start --> y
    abs(dat[0] - dat[3]) +
    # Distance from x --> end
    abs(dat[2] - dat[1]) 
)
# Walking
dist.append(
    abs(dat[0] - dat[1])
)

f = open("teleport.out", "w")
f.write(str(min(dist)))
f.close()





































""" # -*- coding: utf-8 -*-

# Open file
f = open("teleport.in" ,"r")

# describes the amount of piles of manure there are. 
manureCount = int(f.readline())

# Manure data:
manureDat = []


for i in range(manureCount):
    # 
    
    line = f.readline()
    line = line.strip()
    line = line.split(" ")
    line = list(map(int, line))

    manureDat.append(line)


# get starting point for brute force

currMin = 0

for i in manureDat:
    if i[1] < currMin:
        currMin = i[1]

currMax = 0

for i in manureDat:
    if i[1] > currMax:
        currMax = i[1]



def takeTeleporter(telePos, manure):
    # Check if route to teleporter is shorter than route normally. 
    tele = abs(telePos - manure[1])
    nor = abs(manure[0] - manure[1])

    if tele > nor:
        return False
    elif tele < nor:
        return True
    return True






moveDat = []

for i in range(currMin, currMax + 1):
    # assume that i is the teleporter location. 
    print(str(i) + "---------------")
    totalDist = 0
    for j in manureDat:
        
        if takeTeleporter(i, j):
            print("Take teleport: ", end=" ")
            # Get distance to teleporter. 
            dist = abs(j[0]) + abs(i - j[1])
        else:
            print("Walk: ", end=" ")
            # Get distance normally:
            dist = abs(j[0] - j[1])
        print(dist)
        totalDist += dist
    moveDat.append(totalDist)

f = open("teleport.out", "w")
f.write(str(min(moveDat)))
f.close() """