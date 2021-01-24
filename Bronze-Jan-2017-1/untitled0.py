# -*- coding: utf-8 -*-

f = open("notlast.in","r")
a = int(f.readline())
COWS = ["Bessie", "Elsie" , "Daisy", "Gertie", "Annabelle", "Maggie", "Henrietta"]


data = []

for i in range(a):
    data.append(list(f.readline().split()))
    
f.close()
b = {}

for i in data:
    if i[0] not in b:
        b[i[0]] = int(i[1])
    else:
        b[i[0]] += int(i[1])



print(b)
names = []
values = []
for i in b:
    names.append(i)
    values.append(int(b[i]))
for i in COWS:
    if i not in names:
        names.append(i)
        values.append(0)
b = {}
if len(values) > 0:
    
    m = min(values)
    
    if values.count(m) > 1:
        # too many small ones
        for i in range(values.count(m)):
            e = values.index(m)
            values.pop(e)
            names.pop(e)
    else:
        # 1 small value
        e = values.index(m)
        values.pop(e)
        names.pop(e)
    
    f = open("notlast.out","w")
    
    if len(values) > 0:
        m = min(values)
        
        if values.count(m) > 1:
            f.write("Tie\n")
        else:
            f.write(names[values.index(m)] + "\n")
    else:
        f.write("Tie\n")
    f.close()
else:
    f = open("notlast.out","w")
    f.write("Tie\n")
    f.close()