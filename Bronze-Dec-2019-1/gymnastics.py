## -*- coding: utf-8 -*-
f = open("gymnastics.in","r")
dat = []
ans = []
temp = []
kn = list(map(int, f.readline().split(" ")))
for i in range(kn[0]):
    dat.append(list(map(int, f.readline().split(" "))))
f.close()
for i in range(len(dat[0])):
    for j in range(i+1,len(dat[0])):
        ans.append([dat[0][i],dat[0][j]])
for L in dat:
    for i in range(len(L)):
        for j in range(i+1,len(L)):
            
            temp.append([L[i],L[j]])
    print(temp, ans)
    ans = [x for x in temp if x in ans]
    temp = []
f = open("gymnastics.out","w")

f.write(str(len(ans))+"\n")
f.close()
#def before(lis, num1, num2):
#    if (lis.index(num1) < lis.index(num2)):
#        return True
#    else:
#        return False
#for a in range(kn[0]):
#    for b in range(kn[0]):
#        for i in dat:
#            if a == b:
#                continue
#            
#            if before(i, a+1, b+1):
#                if (a+1, b+1) not in ans:
#                    print("added",i, a+1, b+1)
#                    ans.append((a+1, b+1))
#            else:
#                try:
#                    print("removed",i, a+1, b+1)
#                    ans.remove((a+1, b+1))
#                except:
#                    pass
#print(ans)
#anscopy = ans.copy()
#for i in anscopy:
#    print(i)
#    for b in dat:
#        if before(b, i[0], i[1]):
#            print("pass", i)
#            continue
#        else:
#            try:
#                print("removed", i)
#                ans.remove((i[0], i[1]))
#            except:
#                print("error", i)
#                pass
