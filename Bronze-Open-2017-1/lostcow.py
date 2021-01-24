# -*- coding: utf-8 -*-

# ------------------------------------
# SET VARIABLES
# Sets all variables needed for the 
# program to run. 
# ------------------------------------
# open the file. 
f = open("lostcow.in", "r")
temp = list(map(int, f.readline().split(" ")))

# list of movements. 
moveList = [1]

fjPos = temp[0]
bPos = temp[1]
f.close()


# ------------------------------------
# NORMALIZE
# Set's fj's pos to 0, and 
# subtracts the appropriate amount
# from bessie's pos. 
# ------------------------------------
bPos = bPos - fjPos
fjPos = 0
print(bPos, fjPos)

# ------------------------------------
# GENERATE LIST
# Generate list [1, -2, 4, -8] up to
# whatever bPos is. 
# ------------------------------------



def isPositive(num):
    return num >= 0


def shouldContinue(lastValue, bessiePos):
    if isPositive(lastValue) != isPositive(bessiePos):
        return True
    # ok they're the same. 
    if lastValue < 0:
        print(lastValue, bessiePos, lastValue <= bessiePos, "negative")
        return not lastValue <= bessiePos
    elif lastValue > 0:
        print(lastValue >= bessiePos, "positive")
        return not lastValue >= bessiePos





lastValue = 1
while (shouldContinue(lastValue, bPos)):
    moveList.append(lastValue * -2)
    lastValue *= -2

print(lastValue, moveList)

# ------------------------------------
# GET INDEX
# Get where farmer john which STEP
# fj is going to see bessie. 
# ------------------------------------

positive = bPos > 0

for step in range(len(moveList)):
    if (moveList[step] < 0 and positive or
        moveList[step] > 0 and not positive):
        # hey, that's the wrong direction . 
        continue
    if moveList[step] <= 0:
        # negative. 
        if moveList[step] <= bPos:
            # Ok, it's this step. 
            break
    if moveList[step] > 0:
        if moveList[step] >= bPos:
            # Ok, it's this one. 
            break

moveList = moveList[:step+1]
# print("stopped making list at :" + str(step))

# ------------------------------------
# SUM
# Sum totals up to step
# ------------------------------------

# using step

total = 0


for step in range(len(moveList)):
    # also add the previous step. 
    total += abs(moveList[step])
    if step == 0:
        continue
    total += abs(moveList[step - 1])


# ------------------------------------
# REMOVE EXCESS
# FJ may overshoot, so remove where
# fj overshootes. 
# ------------------------------------


lastStep = moveList[-1]

overshoot = abs(lastStep - bPos)

total -= overshoot

# ------------------------------------
# WRITE TO FILE
# Write the output to lostcow.out
# ------------------------------------

f = open("lostcow.out", "w")
f.write(str(total) + "\n")
f.close()





























# older program below. ""



#def initProgram():
#    # should be global. 
#    global fjLoc, bLoc, move, distanceMoved, toMove, initfjLoc
#    global prevPos, moveList
#    
#    
#    
#    f = open("lostcow.in" ,"r")
#    # it moves starting at 1. 
#    move = 1
#    # 
#    distanceMoved = 0
#    moveList = []
#    toMove = 1
#    
#    # list for details on b and fj's loc. 
#    dea = list(map(int, f.readline().split(" ")))
#    
#    # FJ's loc is at the first num. 
#    fjLoc = dea[0]
#    prevPos = dea[0]
#    # for the initial location
#    initfjLoc = dea[0]
#    # bessie's loc is at the second num. 
#    bLoc = dea[1]

#def updateMove():
#    global move
#    # update how far fj should move. 
#    # inverse the sign. 
#    move = -move
#    # and double the distance .
#    move = move * 2
##    print("move is now " + str(move))
#
#
#
#
#def moveFJ():
#    global fjLoc, distanceMoved, prevPos
##    print("moving fj " + str(toMove))
#    # take move and add it onto fj's loc.
#    prevPos = fjLoc
#    fjLoc += toMove
#    
#    # move should be positive. 
#    distanceMoved += abs(toMove)
#    print("we are now at " + 
#          str(fjLoc) + 
#          " and we have moved " + 
#          str(distanceMoved) + 
#          " and we were supposed to move " +
#          str(toMove) + 
#          " move: " + 
#          str(move))
#
#def calcToMove():
#    global toMove
#    # calculate how much we should move. 
#    # remember, we are moving to position x + move
#    # find how far up we are from the initial pos. 
#    toMove = abs(fjLoc - getDestPos())
#    if fjLoc > getDestPos():
#        # we are supposed to be moving backwards! 
#        toMove = toMove * -1
#
#def getDestPos():
#    # get the destination! 
#    return initfjLoc + move
#
#
#
#def hasntSeenBessie():
#    global prevPos, fjLoc
#    # check if bessie is in between these prevPos and fjLoc
#    if (
#        bLoc < fjLoc and bLoc > prevPos
#        or
#        bLoc > fjLoc and bLoc < prevPos
#        or
#        bLoc == fjLoc
#        or
#        bLoc == prevPos
#        ):
#        return True
#    return False
#
#def dealWithExtra():
#    global distanceMoved, aboutToBeSubtracted
#    # subtract the overshoot-ed distance
#    # from the total distance moved. 
#    if fjLoc <= bLoc:
#        # Subtract. 
#        aboutToBeSubtracted = abs(fjLoc) - abs(bLoc)
#        distanceMoved -= aboutToBeSubtracted
#    elif fjLoc >= bLoc:
#        aboutToBeSubtracted = fjLoc - bLoc
#        distanceMoved -= aboutToBeSubtracted
#    
#
#def writeToFile():
#    f = open("lostcow.out" ,"w")
#    f.write(str(distanceMoved) + "\n")
#    f.close()
#
#
#
#initProgram()
## TODO: Deal with fj over shooting where
## bessie is at. 
#while not hasntSeenBessie(): # <= done
#    moveFJ()
#    updateMove()
#    calcToMove()
## TODO: enable this. 
#dealWithExtra()
#
#writeToFile()
#print(distanceMoved)




