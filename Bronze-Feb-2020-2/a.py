f = open("breedflip.in", "r")
N = int(f.readline())
string1 = f.readline()
string2 = f.readline()
f.close()
newString = ""

for i in range(len(string1)):
    if string1[i] == string2[i]:
        newString = newString + "X"
        continue
    else:
        # different
        newString = newString + "S"

ans = 0
print(newString)
for i in range(len(newString)):
    if newString[i] != newString[i-1] and newString[i] != "X":
        ans = ans + 1
    else:
        continue

f = open("breedflip.out", "w")
f.write(str(ans)+"\n")
f.close()

