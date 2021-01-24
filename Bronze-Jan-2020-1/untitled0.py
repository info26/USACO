

f = open("word.in" , "r")
curline= 0
N,K = map(int, f.readline().split())
words = list( f.readline().strip().split())
f.close()
print(words)

f = open("word.out", "w")
for word in words:
    if curline+len(word) > K:
        f.write("\n")
        f.write(word)
        curline = len(word)
    else:
        if curline == 0:
            f.write(word)
            
        else:
            f.write(" " + word)
        curline = curline + len(word)
#for i in range(len(words)):
#    if curline + len(words[i]) <= a[1]:
#        f.write(words[i])
#        #can we fit anymore words on this line? if so, then set curline
#        #and continue. 
#        #if not, then print a new line, set curline to 0 and continue
#        try:
#            if len(words[i+1]) + len(words[i]) < a[1]:
#                curline = curline + len(words[i])
#                continue
#            elif len(words[i+1]) + len(words[i]) == a[1]:
#                f.write(" ")
#                curline = curline + len(words[i])
#                continue
#            else:
#                f.write("\n")
#                curline = 0
#        except:
#            pass
#    else:
#        f.write("\n")
#        f.write(words[i])
#        curline = len(words[i])
#        if curline + len(words[i+1]) <= a[1]:
#            f.write(" ")
f.write("\n")
f.close()





