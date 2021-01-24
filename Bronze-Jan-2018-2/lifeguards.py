#################
# lifeguards.py #
#################

f = open("lifeguards.in")
n = int(f.readline())
lifeguards = []
for i in range(n):
    line = f.readline()
    # default: " "
    line = line.split()
    line = map(int, line)
    line = list(line)
    lifeguards.append(line)
f.close()

###########################################################################
# Sort lifeguards by time they START duty.
lifeguards.sort(key = lambda key: key[0])

events = []

## Produce events
for i in range(len(lifeguards)):
    event = {"action": "on", "time": lifeguards[i][0], "id": i}
    events.append(event)
    event = {"action": "off", "time": lifeguards[i][1], "id": i}
    events.append(event)
events.sort(key = lambda key: key["time"])



# Decrements or increments the value in the range specified.
# f = number to start at
# t = number to end at (NOT INCLUSIVE)
# modifier = what to add to each number in the range.
def modifyInRange(f, t, modifier):
    global track
    # To is exclusive, because if a lifeguard goes from
    # 4 -> 7, the 7 is not counted.
    # 4 -> 7 = 3 units of time.
    for i in range(f, t):
        track[i] += modifier



# Counts the number of units in 'track' that are
# not 0.
# returns how many units are not 0.
def countTotalUnitsNot0():
    global track
    counter = 0
    for i in track:
        if i != 0:
            counter += 1
    return counter



# First, go from 1 -> 1000, tracking the number of lifeguards
# working at each time unit.

track = [0] * 1000

for timeRange in lifeguards:
    modifyInRange(timeRange[0], timeRange[1], 1)

maxTimeCovered = -1


for lifeguardRemoved in lifeguards:
    # assume lifeguardRemoved is the lifeguard
    # that is fired, so decrement in that range.
    modifyInRange(lifeguardRemoved[0], lifeguardRemoved[1], -1)
    # now, let's get the total units covered, after
    # we've decremented stuff .
    unitsCovered = countTotalUnitsNot0();
    if unitsCovered > maxTimeCovered:
        maxTimeCovered = unitsCovered
    # reincrement it up. (is that a word?) (no don't think so)
    modifyInRange(lifeguardRemoved[0], lifeguardRemoved[1], 1)


f = open("lifeguards.out", "w")
f.write(str(maxTimeCovered) + "\n")
f.close()
