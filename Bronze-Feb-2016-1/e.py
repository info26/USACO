f = open("pails.in", "r")
a = list(map(int, f.readline().split(" ")))
f.close()

looptimes =  a[2] // (min(a[0],a[1]))
looptimes += 1
dat = []
if (max(a[0],a[1]) == a[1]):
    a0times = 0
    a1times = looptimes
else:
    a1times = 0
    a0times = looptimes

for c in range(looptimes):
    for i in range(looptimes):
        temp = (a[0] * c) + (a[1] * i)
        print(temp)
        if (temp <= a[2]):
            dat.append(temp)
            


f = open("pails.out","w")
f.write(str(max(dat)))
f.close()