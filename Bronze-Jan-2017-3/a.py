f = open("cowtip.in");
n = int(f.readline())
board = []
for i in range(n):
    board.append(
        list(
            map(int, 
                list(
                    f.readline().strip()
                )
            )
        )
    )
f.close()



# this function finds the position that is the bottom most, left most that is tipped. 
# 0 = [0,1,2,3,4]
# 1 = [0,1,2,3,4]
# 2 = [0,1,2,3,4]
# 3 = [0,1,2,3,4]
# 4 = [0,1,2,3,4]

def getNext():
    x = len(board[0]) - 1
    y = len(board) - 1

    while True:
        while True:
            if board[y][x] == 1:
                # this is tipped. 
                #print("found" + str(x) + " " + str(y))
                return (x,y)
            # move the cursor "left" one position
            x -= 1
            if x < 0:
                x = len(board[0]) - 1
                y -= 1
                break
        if y < 0:
            break
    return False
def flip(x,y):
    global board
    if board[y][x] == 0:
        board[y][x] = 1
    else:
        board[y][x] = 0
def execute(xy):
    x = xy[0]
    y = xy[1]
    # start from the corner, and flip each pos. 
    for a in range(x + 1):
        for b in range(y + 1):
            #print("flip " + str((a,b)))
            flip(a,b)
####################################################
# main                                             #
####################################################
count = 0
res = getNext()
if res != False:
    while (res != False):
        execute(res)
        res = getNext()
        count += 1


f = open("cowtip.out", "w")
f.write(str(count) + "\n")
f.close()