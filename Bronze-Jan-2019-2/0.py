f = open("sleepy.in", "r")
cows = int(f.readline().strip())
cowOrder = list(map(int, f.readline().strip().split()))
f.close()

i = cows - 1
while i>0 and cowOrder[i] > cowOrder[i-1]:
    i -= 1
print(i)
streak = 0
for ind, val in enumerate(cowOrder):
    if ind == 0:
        # automatically increase, we can't see anything!
        streak += 1
        continue
    
    if cowOrder[ind - 1] < val:
        # Great! We are going up. 
        streak += 1
    else:
        # Oops, streak lost!  
        
        streak = 1 # (1 because this counts as a number in the new streak)

f = open("sleepy.out", "w")
f.write(str( len(cowOrder) - streak ) + "\n")
f.close()