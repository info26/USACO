f = open("hps.in", "r")
dat = []
for i in range(int(f.readline())):
    dat.append(list(map(int, f.readline().strip().split())))
f.close()

def won(challenger, defender):
    mappings = {
        "hoof": ["scissors"],
        "paper": ["hoof"],
        "scissors": ["paper"]
    }

    return defender in mappings[challenger]

maxWins = 0

for hoof in range(1, 4):
    newList = [1,2,3]
    newList.remove(hoof)
    for paper in newList:
        wins = 0 
        # now, let's do it.
        newnewList = newList.copy()
        newnewList.remove(paper)
        mapping = {
            hoof: "hoof",
            paper: "paper",
            newnewList[0]: "scissors"
        }

        for verse in dat:
            result = won( mapping[verse[0]], mapping[verse[1]] )
            if result:
                wins += 1
        
        if wins > maxWins:
            maxWins = wins

f = open("hps.out", "w")
f.write(str(maxWins) + "\n")
f.close()