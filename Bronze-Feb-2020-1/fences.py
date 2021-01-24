triangles = []


def checkValidity(triangle):
    #x check
    xs = [triangle[0][0], triangle[1][0], triangle[2][0]]
    temp = set(xs)
    if len(temp) == 2:
        # passed, and continue
        pass
    else:
        return False
    #y check
    ys = [triangle[0][1], triangle[1][1], triangle[2][1]]
    temp = set(ys)
    if len(temp) == 2:
        # passed
        return True
    return False


def triangleArea(triangle):
    # x calculation
    if triangle[0][0] != triangle[1][0]:
        x1 = triangle[0]
        x2 = triangle[1]
    elif triangle[0][0] != triangle[2][0]:
        x1 = triangle[0]
        x2 = triangle[2]
    elif triangle[1][0] != triangle[2][0]:
        x1 = triangle[1]
        x2 = triangle[2]
    xcalc = abs(x1[0] - x2[0])
    # y calculation
    if triangle[0][1] != triangle[1][1]:
        y1 = triangle[0]
        y2 = triangle[1]
    elif triangle[0][1] != triangle[2][1]:
        y1 = triangle[0]
        y2 = triangle[2]
    elif triangle[1][1] != triangle[2][1]:
        y1 = triangle[1]
        y2 = triangle[2]
    ycalc = abs(y1[1] - y2[1])
    return (xcalc * ycalc) / 2


# input
f = open("triangles.in", "r")
fences = int(f.readline())
fencedata = []
possibilities = []
for i in range(fences):
    temp = list(map(int, f.readline().split(" ")))
    fencedata.append((temp[0], temp[1]))
f.close()
#first for loop
for f1 in fencedata:
    #second for loop
    for f2 in fencedata:
        #third
        for f3 in fencedata:
            if f1 == f2 or f2 == f3 or f3 == f1:
                continue
            possibilities.append((f1, f2, f3))
revised = []
for i in possibilities:
    a = checkValidity(i)
    if a:
        revised.append(i)
#remove memory
possibilities = None
max = 0
for i in revised:
    temp = triangleArea(i)
    if temp > max:
        max = temp
f = open("triangles.out", "w")
if max.is_integer:
    f.write(str(int(max * 2)))
else:
    f.write(str(max * 2))
f.write("\n")
f.close()
