f = open("whereami.in","r")
a = int(f.readline())
dat = f.readline()
f.close()
i = 0
tem = []
brea = False
for b in range(len(dat)+1):
    tempset = set()
    for b in range(len(dat)+2):
        if b < i-1:
            continue
        if b-i < 0 or b < 0:
            continue
        temp = dat[b-i:b]
        if temp in tempset:
            brea = True
            tempset.add("BREAK")
            break
        if len(temp) == i:
            tempset.add(temp)
        else:
            continue
    #print(tempset)
    if 'BREAK' in tempset:
        pass
    else:
        ans = i
        break
    #print("BREAK" in tempset)
    i += 1
    brea = False
f = open("whereami.out","w")
f.write(str(ans))
f.write("\n")
f.close()