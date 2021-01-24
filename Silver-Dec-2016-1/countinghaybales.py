def upper_index(n):
    l = 0
    r = len(loc)
    while l<r:
        mid = (l+r)//2
        if loc[mid] == n:
            return mid
        elif loc[mid]<n:
            l = mid+1
        else:
            r = mid
    return l

f = open("haybales.in","r")
settings =list(map(int, f.readline().strip().split()))
loc = list(map(int, f.readline().strip().split()))
loc.append(10000000001)
loc.sort()
que = []
result = []
tempres = 0
for i in range(settings[1]):
    que.append(list(map(int, f.readline().strip().split())))
f.close()
for i in que:
    result.append(upper_index(i[1]+1) - upper_index(i[0]))
f = open("haybales.out","w")
f.write("\n".join(list(map(str, result)))+"\n")
f.close()
