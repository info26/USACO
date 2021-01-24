import copy

f = open("backforth.in", "r")
barn1 = list(map(int, f.readline().strip().split()))
barn2 = list(map(int, f.readline().strip().split()))
f.close()
# ==================================================

ans = []

def recurse(iterations, barnNum, curDelta, barnState):
    global ans
    origBarnNum = barnNum
    origcurDelta = curDelta

    barn = {1: barnState[0], 2: barnState[1]}[barnNum]
    if iterations == 0:
        # We are done!
        ans.append(curDelta)
        return
    for i in set(barn):

        barnNum = origBarnNum
        curDelta = origcurDelta
        if barnNum == 1:
            # we are taking it away
            curDelta -= i
            state = copy.deepcopy(barnState)
            state[1].append(i)
            state[0].remove(i)

            barnNum = 2
        elif barnNum == 2:
            # we are moving it here
            curDelta += i
            state = copy.deepcopy(barnState)
            state[0].append(i)
            state[1].remove(i)
            barnNum = 1
        
        recurse(iterations - 1, barnNum, curDelta, state)


state = [barn1, barn2]
recurse(4, 1, 0, copy.deepcopy(state))

f = open("backforth.out", "w")
f.write(str(len(set(ans))) + "\n")
f.close()