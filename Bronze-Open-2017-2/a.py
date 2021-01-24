f = open("cownomics.in")
a,b = list(map(int, f.readline().strip().split()))
spots = []
nospots = []
for i in range(a):
    spots.append(f.readline().strip())
for i in range(a):
    nospots.append(f.readline().strip())
f.close()
count = 0
for i in range(b):
    # assume i is the position which determines
    # if a cow has spots or not.
    spotsGenomes = set()
    nospotsGenomes = set()
    for cow in spots:
        spotsGenomes.add(cow[i])
    for cow in nospots:
        nospotsGenomes.add(cow[i])
    comb = spotsGenomes & nospotsGenomes
    if len(comb) == 0:
        count += 1
f = open("cownomics.out", "w")
f.write(str(count) + "\n")
f.close()
