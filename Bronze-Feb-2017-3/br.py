



# -----------------------
# 1. read input
# -----------------------
f = open("cowqueue.in", "r")
cows = int(f.readline().strip())
data = []
for i in range(cows):
    readin = f.readline()
    readin = readin.strip()
    readin = readin.split(" ")
    readin = map(int, readin)
    readin = list(readin)
    data.append(readin)
# print(data)

# -----------------------
# 2. sort list
# -----------------------

# WOW sorting by key so fancy
data.sort(key=lambda cow: cow[0])
print(data)
# -----------------------
# 3. loop through input
# -----------------------

clock = 0



for cowCrossing in range(len(data)):
    if cowCrossing == 0:
        clock = sum(data[cowCrossing])
    elif data[cowCrossing][0] > clock:
        clock = sum(data[cowCrossing])
    elif data[cowCrossing][0] < clock:
        clock += data[cowCrossing][1]






# # the bulk of the program is here! 
# for cowCrossing in range(len(data)):
#     # add processing time
#     totalTime += data[cowCrossing][1]
#     # print("added " + str(data[cowCrossing][1]) + " prcoessing")

#     if cowCrossing == 0:
#         totalTime += data[cowCrossing][0]
#         continue
#     # add delta time to last cowcrossing
#     # get last cowcrossing
#     previous = data[cowCrossing-1]
#     # only do this if the time does not intercept the last one. 
#     if data[cowCrossing][0] > (previous[0] + previous[1]):
        
#         # and subtract!
#         totalTime += abs(data[cowCrossing][0] - (previous[0] + previous[1]))
#         # print("added " + str(abs(data[cowCrossing][0] - previous[0])) + " delta")

# print(totalTime)
# 4. write

f = open("cowqueue.out", "w")
f.write(str(clock))
f.close()