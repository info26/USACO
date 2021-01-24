f = open("hps.in", "r")
N = int(f.readline().strip())
dat = []
for i in range(N):
    dat.append(f.readline().strip())
f.close()

# probably my most clever way so far
# to determine a winner.
def win(me, opponent):
    mapping = {
        "H": "S",
        "P": "H",
        "S": "P"
    }

    return mapping[me] == opponent



H = []
P = []
S = []

dat.reverse()

lastH = 0
lastP = 0
lastS = 0

for i in dat:
    # H
    if win("H", i):
        lastH += 1
    
    # P
    if win("P", i):
        lastP += 1
    
    # S
    if win("S", i):
        lastS += 1
    
    H.append(lastH)
    P.append(lastP)
    S.append(lastS)


H.reverse()
P.reverse()
S.reverse()

dynList = {
    "H": H,
    "P": P,
    "S": S
}

maxChange = 0

for starting in ["H", "P", "S"]:
    changePossibilities = ["H", "P", "S"]
    changePossibilities.remove(starting)
    for changeTo in changePossibilities:
        for changeNum in range(len(dat)):
            startingChange = (dynList[starting][0] - dynList[starting][changeNum])
            secondChange = dynList[changeTo][changeNum]

            totalChange = startingChange + secondChange
            if totalChange > maxChange:
                maxChange = totalChange

f = open("hps.out", "w")
f.write(str(maxChange) + "\n")
f.close()