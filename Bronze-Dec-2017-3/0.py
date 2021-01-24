file = open("measurement.in")
logs = int(file.readline())
log = []
for i in range(logs):
    e = file.readline().split()
    # the day(s) number to be int so we can
    # sort by it. 
    e[0] = int(e[0])
    e[2] = int(e[2])
    log.append(e)
log.sort(key = lambda x: x[0])





def getMax():
    global curr
    maxx = None
    maxnum = -1
    for key in curr:
        if curr[key] > maxnum:
            maxx = key
            maxnum = curr[key]
        elif curr[key] == maxnum:
            if type(maxx) != set:
                # convert to set
                temp = maxx
                maxx = set()
                maxx.add(temp)
                maxx.add(key)
            else:
                maxx.add(key)
    return maxx




curr = {
    "Bessie": 7,
    "Mildred": 7,
    "Elsie": 7
}
top = {"Bessie", "Mildred", "Elsie"}
change = 0
for i in log:
    # Ok, let's apply the change. 
    curr[i[1]] += i[2]
    
    temp = getMax()
    if temp != top:
        # CHANGE!
        change += 1
        top = temp

f = open("measurement.out", "w")
f.write(str(change))
f.close()
    
