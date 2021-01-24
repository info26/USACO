# -*- coding: utf-8 -*-



def getletters(words):
    let = "".join(words)
    let = set(let)
    temp = {}
    for i in let:
        temp[i] = 0
    for a in words:
        for b in let:
            if b in temp and a.count(b) > temp[b]:
                temp[b] = a.count(b)
    return temp

def mergeDictAdd(dict1, dict2):
    temp = {}
    for key in dict1:
        if key in dict2:
            temp[key] = dict1[key] + dict2[key]
        else:
            #key is not in dict2
            temp[key] = dict1[key]
    for key in dict2:
        if key in dict1:
            #already handled by for loop above:
            continue
        else:
            #key not in dict1
            #special case
            temp[key] = dict2[key]
    return temp

ans = {}
wordsToProcess = []
f = open("blocks.in", "r")
n = int(f.readline())
for i in range(n):
    wordsToProcess.append(list(f.readline().split()))
f.close()
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
for i in wordsToProcess:
    a = getletters(i)
    ans = mergeDictAdd(a, ans)
    

f = open("blocks.out", "w")
for i in letters:
    if i in ans:
        f.write(str(ans[i]) + "\n")
    else:
        f.write("0\n")

f.close()