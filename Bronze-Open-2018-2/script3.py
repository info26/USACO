def readList(file):
    string = file.readline()
    string = string.strip().split(" ")
    string = map(int, string)
    string = list(string)
    return string


f = open("milkorder.in")
info = readList(f)
order = readList(f)
require = {}
for i in range(info[2]):
    temp = readList(f)
    require[temp[0]] = temp[1]
############################################

working = [-1] * (info[0])
# fill in the required positions. 
for cow in require:
    working[require[cow] - 1] = cow


def getChunks():
    # chunks = list of lists, contained in the following format. 
    # [start (inclusive), end (not inclusive), required numbers]
    chunks = []

    # intersection
    intersect = []
    # populate the intersection
    for i in working:
        if i in order:
            intersect.append(i)
    print(intersect)
    # 1. find the **first** intersect
    # 2. if there are order(s) required to be before it, create a chunk.
    for ind, val in enumerate(order):
        if val in working:
            # Great, so let's create a chunk if there are cows
            # required to be before it. 
            if (ind != 0):
                chunks.append(
                    [0, working.index(val), order[0: ind]]
                )
            break
    
    for ind, val in enumerate(intersect):
        if ind != len(intersect) - 1:

            neighborIndex = working.index(intersect[ intersect.index( val ) + 1 ])
            neighborOrderIndex = order.index( intersect[ intersect.index( val ) + 1 ] )
        else:
            neighborIndex = len(working)
            neighborOrderIndex = len(order)
        # Let's find where this starts and ends. 
        start = working.index(val) # obviously, this chunk starts where this order starts. 
        if ind == len(intersect) - 1:
            # well, we're at the end, so this must be just len(working)
            end = len(working)
        else:
            # next intersection's index
            end = neighborIndex
        chunks.append(
            [start, end, order[ order.index(val) + 1:neighborOrderIndex ]]
        )
    if len(chunks) == 0:
        # well, nothing can be made, so just insert one with the whole entire thing. 
        chunks.append(
            [0, len(working), order]
        )
    return chunks

def findFirstAvailable(ind):
    pointer = ind
    while True:
        if working[pointer] == -1: # free space!
            return pointer
        pointer += 1
    raise UnicodeDecodeError("something happened! ")

def findFirstAvailableBackwards(ind):
    pointer = ind
    while True:
        pointer -= 1
        if working[pointer] == -1: #free space!
            return pointer
    raise UnicodeDecodeError("something happened! ")


print(working)
chunks = getChunks()
oneSwitch = 1 in order
findFunc = {
    True: findFirstAvailable,
    False: findFirstAvailableBackwards
}[oneSwitch] # WHOA! It'S AN INLINE DICTIONARY. Cool. 
for chunk in chunks:
    area = working[chunk[0]: chunk[1]]
    # chunk[2] contains all the numbers that have to fit
    if oneSwitch:
        fit = chunk[2]
    else:
        chunk[2].reverse()
        fit = chunk[2]
    
    # now, we shall start making attempts to fill this chunk it
    for i in fit:
        if oneSwitch:
            nextAvailArea = findFunc(chunk[0])
        else:
            nextAvailArea = findFunc(chunk[1])
        if i in working:
            continue
        working[nextAvailArea] = i

print(working, chunks)

if oneSwitch:
    ans = working.index(1) # soo, find where the 1 landed. 
else:
    ans = working.index(-1) # find first available spot

f = open("milkorder.out", "w")
f.write(str(ans + 1) + "\n")
f.close()