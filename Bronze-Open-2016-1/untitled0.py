f = open("diamond.in" ,"r")
a = list(map(int, f.readline().split(" ")))
dat = []
ans = []
for i in range(a[0]):
    dat.append(int(f.readline()))
f.close()

def objinlist(mini, maxa):
    count = 0
    for i in dat:
        if i >= mini and i <= maxa:
            count += 1
    return count

for obj in dat:
    e = objinlist(obj, obj+a[1])
    ans.append(e)
    
f = open("diamond.out" ,"w")
f.write(str(max(ans)))
f.close()