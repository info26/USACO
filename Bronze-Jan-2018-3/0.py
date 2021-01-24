f = open("outofplace.in", "r")
e = int(f.readline())
dat = []
for i in range(e):
    dat.append(int(f.readline()))
f.close()

unsorted = dat.copy()
dat.sort()
sorted = dat

diff = -1

print(unsorted)
print(sorted)

for i in range(len(sorted)):
    if sorted[i] != unsorted[i]:
        diff += 1

f = open("outofplace.out", "w")
diff = max(0, diff)
f.write(str(diff) + "\n")

f.close()


# 2 4 7 7 9 3
# 2 4 7 7 3 9
# 2 4 3 7 7 9
