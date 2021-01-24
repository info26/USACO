f = open("cowsignal.in", "r")
meta = f.readline().split()
meta = list(map(int, meta))

dat = []

 

for i in range(meta[0]):
    dat.append(f.readline().strip())


f.close()


produced = []

for i in dat:
    toAppend = ""
    for b in i:
        for a in range(meta[2]):
            toAppend += b
    produced.append(toAppend)
    
    
toReplace = []

for i in produced:
    for a in range(meta[2]):
        toReplace.append(i)

produced = toReplace

f = open("cowsignal.out", "w")
for i in produced:
    f.write(i + "\n")
f.close()