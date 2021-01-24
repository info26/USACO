f = open("shell.in","r")
num = int(f.readline().strip())

ans = 0
data = []

for i in range(num):
    data.append(list(map(int, f.readline().strip().split())))
for a in range(1,4):
    loc = a
    temp  = 0
    for i in data:
        if i[0] == loc:
            loc = i[1]
        elif i[1] == loc:
            loc = i[0]
        if loc == i[2]:
            temp += 1
    if temp > ans:
        ans = temp


f.close()
f = open("shell.out","w")
f.write(str(ans)+"\n")
f.close()
