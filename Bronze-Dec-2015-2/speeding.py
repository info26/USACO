# ---------------------
# READ DATA
# ---------------------

file = open("speeding.in")

count = list(map(int, file.readline().split()))

# count[0] = actual speed
# count[1] = bessie speed
actualSpeed = []
bessieSpeed = []

for i in range(count[0]):
    reading = file.readline()
    reading = reading.split()
    reading = map(int, reading)
    reading = list(reading)

    actualSpeed.append(reading)


for i in range(count[1]):
    reading = file.readline()
    reading = reading.split()
    reading = map(int, reading)
    reading = list(reading)

    bessieSpeed.append(reading)

events = []

# events from actual speed
clock = 0

for i in actualSpeed:
    events.append(
        {
            "time": clock,
            "type": "actual",
            "new": i[1],
        }
    )
    # increment clock
    clock += i[0]

clock = 0

for i in bessieSpeed:
    events.append(
        {
            "time": clock,
            "type": "bessie",
            "new": i[1],
        }
    )
    # increment clock
    clock += i[0]

events.sort(key = lambda key: key["time"])



for i in range(len(events)):
    if i == 0:
        continue
    
    prev = events[i-1]
    this = events[i]
    

    if prev["time"] == this["time"]:
        update = {}
        if prev["type"] == "actual":
            update["actual"] = prev["new"]
        if prev["type"] == "bessie":
            update["bessie"] = prev["new"]


        prev["type"] = "bundle"


        if events[i]["type"] == "actual":
            update["actual"] = this["new"]
        if events[i]["type"] == "bessie":
            update["bessie"] = this["new"]

        prev["new"] = update


print(events)

# print(events)



maxOverspeed = 0

# set up initial
bSpeed = bessieSpeed[0][1]
aSpeed = actualSpeed[0][1]

clock = 0
# print(events)
for event in events:
    # remember to update first!
    if event["type"] == "bundle":
        aSpeed = event["new"]["actual"]
        bSpeed = event["new"]["bessie"]
    if event["type"] == "actual":
        aSpeed = event["new"]
    elif event["type"] == "bessie":
        bSpeed = event["new"]
    # Recompare b speed and a speed
    clock = event["time"]
    if bSpeed > aSpeed:
        # print("Overspeed at " + str(clock) + " and bessie driving at " + str(bSpeed) + " with the speed limit being " + str(aSpeed))
        overspeed = bSpeed - aSpeed
        
        # print(overspeed)

        if overspeed > maxOverspeed:
            maxOverspeed = overspeed

f = open("speeding.out", "w")
f.write(str(maxOverspeed))
f.close()