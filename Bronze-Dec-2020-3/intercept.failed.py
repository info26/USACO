N = int(input(""))
dat = []
for b in range(N):
    line = input("")
    line = line.split()
    dat.append({
        "dir": line[0],
        "x": int(line[1]),
        "y": int(line[2]),
        "stopping": {}
    })

ans = [99999999999] * N

def willIntercept(cow1, cow2, accountForStopping = False):
    if cow1["dir"] == cow2["dir"]:
        # they will never intercept. 
        return [False]
    if cow1["dir"] == "N":
        Ncow = cow1
    if cow2["dir"] == "N":
        Ncow = cow2
    if cow1["dir"] == "E":
        Ecow = cow1
    if cow2["dir"] == "E":
        Ecow = cow2
    

    # find time N cow takes to intercept E's path. 
    NtoE = abs(Ncow["y"] - Ecow["y"])
    EtoN = abs(Ncow["x"] - Ecow["x"])
    if accountForStopping:
        NtoE = min(Ncow["stopping"], NtoE)
        EtoN = min(Ecow["stopping"], EtoN)

    
    if NtoE == EtoN:
        # both of them arrive at the same time!
        return [False]
    if NtoE < EtoN:
        return [[cow1, cow2].index(Ncow), EtoN]
    if EtoN < NtoE:
        return [[cow1, cow2].index(Ecow), NtoE]

def fill(cowNum, num):
    cow = dat[cowNum]
    if cow["dir"] == "N":
        newVal = num
    if cow["dir"] == "E":
        newVal = num

    oldVal = cow["stopping"]

    if newVal < oldVal:
        cow["stopping"] = newVal


for challengecow in range(len(dat)):
    for othercow in range(len(dat)):
        if challengecow == othercow: continue

        res = willIntercept(
            dat[challengecow],
            dat[othercow],
        )
        if res[0] == False:
            # no interception, let's continue
            continue
        
        if res[0] == 0:
            # the challenger won!
            fill(othercow, res[1], challengecow)
        
        if res[0] == 1:
            fill(challengecow, res[1], othercow)

for challengecow in range(len(dat)):
    for othercow in range(len(dat)):
        if challengecow == othercow: continue

        res = willIntercept(
            dat[challengecow],
            dat[othercow],
            accountForStopping=True
        )
        print(challengecow, othercow, res, dat[challengecow], dat[othercow])
        if res[0] == False:
            # no interception, let's continue
            continue
        
        if res[0] == 0:
            # the challenger won!
            ans[othercow] = res[1]
        
        if res[0] == 1:
            ans[challengecow] = res[1]
    if ans[challengecow] == 99999999999:
        ans[challengecow] = "Infinity"

print(ans)