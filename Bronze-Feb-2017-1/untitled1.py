f = open("crossroad.in", "r")

cowposinst = []
N = int(f.readline())
for i in range(N):
    cowposinst.append(list(map(int, f.readline().split())))

f.close()

curcowpos = {}
crossing = 0


for i in cowposinst:
    if i[0] not in curcowpos:
        curcowpos[i[0]] = i[1]
    else:
        if i[1] == curcowpos[i[0]]:
            pass
        else:
            crossing = crossing + 1
            curcowpos[i[0]] = i[1]

f = open("crossroad.out", "w")
f.write(str(crossing) + "\n")
f.close()