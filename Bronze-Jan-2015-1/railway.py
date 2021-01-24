f = open("cowroute.in","r")
dat = list(map(int, f.readline().strip().split()))
routeinfo = []
routedata = []
found = 0
res = []
def check(a,b):
    cont = 1
    cont == a[0] in b
    
    if cont == True:
        c = b.index(a[1])
        if a[1] in b[c:] and a[0] in b[:c]:
            return True
    else:
        return False
for i in range(dat[2]):
    routeinfo.append(list(map(int, f.readline().strip().split())))
    routedata.append(list(map(int, f.readline().strip().split())))
f.close()
for i in range(len(routedata)):
    if dat[0] in routedata[i] and dat[1] in routedata[i]:
        if routedata[i].index(dat[0]) < routedata[i].index(dat[1]):
            res.append(routeinfo[i][0])
        else:
            print("fail on second if",i)
    else:
        print("fail on first if",i)
if len(res) == 0:
    answer = -1
else:
    answer = min(res)
f = open("cowroute.out","w")
f.write(str(answer)+"\n")
f.close()
