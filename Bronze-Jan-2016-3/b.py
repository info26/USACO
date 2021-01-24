import sys
sys.stdout = open('log.txt', 'w')
f = open("mowing.in", "r")
# why is there not a variable determining how many lines there are? 
# oh well, we have to determine it ourselves. 
count = len(f.readlines())
f.seek(0)
n = int(f.readline().strip())
moves = []
for i in range(count - 1):
    line = f.readline()
    action = line.split()
    moves.append({
        "dir": action[0], 
        "dist": int(action[1]) # convert to int here. 
    })
f.close()

class Grid:
    def __init__(self):
        self.dict = {}
    def get(self, xy):
        if xy not in self.dict:
            self.dict[xy] = -1
        return self.dict[xy]
    def set(self, xy, val):
        self.dict[xy] = val


grid = Grid() # not the best, i know. 


def getStepped(move):
    tempFJ = farmerJohn.copy()
    gen = []
    if move["dir"] in ["N", "S"]:
        # we are moving up and down, 
        # so we are making changes to y dir
        increment = {"N": 1, "S": -1}[move["dir"]]
        for i in range(move["dist"]):
            tempFJ["y"] += increment
            gen.append((tempFJ["x"], tempFJ["y"]))

    elif move["dir"] in ["E", "W"]:
        # we are making changes to x dir.
        increment = {"E": 1, "W": -1}[move["dir"]] # whoa! inline dictionary. 
        for i in range(move["dist"]):
            tempFJ["x"] += increment
            gen.append((tempFJ["x"], tempFJ["y"]))

    return gen

def incFJ(move):
    global farmerJohn
    if move["dir"] in ["N", "S"]:
        incr = {"N": 1, "S": -1}[move["dir"]]
        incr *= move["dist"]
        farmerJohn["y"] += incr
    elif move["dir"] in ["E", "W"]:
        incr = {"E": 1, "W": -1}[move["dir"]]
        incr *= move["dist"]
        farmerJohn["x"] += incr

        



farmerJohn = {
    "x": 0,
    "y": 0,
    "time": 0
}

curGrowbackTime = 9999999999999

for move in moves:
    #print("MOVE---------------------------------------------------")
    #print("Move: " + str(move))
    # now simulate. 
    # we are gonna pretend farmerjohn is on 0,0 to begin. 
    # no need to worry about negative values, because we are saving memory using tuples and a dict, to only store what is needed. 
    for stepped in getStepped(move):
        farmerJohn["time"] += 1


        if grid.get(stepped) == -1:
            # fj hasn't been here before. 
            grid.set(stepped, farmerJohn["time"])
        else:
            # farmer john has been here before. 
            calc = farmerJohn["time"] - grid.get(stepped)
            if calc < curGrowbackTime:
                #print("Just stepped on visited cell!" )
                #print("Cell Location: " + str(stepped))
                #print("Last Visited Time: " + str(grid.get(stepped)))
                #print("Time: " + str(farmerJohn['time']))

                curGrowbackTime = calc
            grid.set(stepped, farmerJohn["time"])
        
        
        # increment time
        
    incFJ(move)
    
    
    #print("FJ After Move: " + str(farmerJohn))
    #print("MOVE---------------------------------------------------")
if (curGrowbackTime == 9999999999999):
    curGrowbackTime = -1


f = open("mowing.out", "w")
f.write(str(curGrowbackTime))
f.close()

