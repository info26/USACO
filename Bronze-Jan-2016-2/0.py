def explodeHaybale(causeIndex, exploded, radius, treated, new):

    #global haybales
    #print("CALLED!" + str(haybales[causeIndex]) + " RADIUS: " + str(radius))
    exploded.add(causeIndex)
    treated.add(haybales[causeIndex])
    # treated.add(causeIndex)
    searchLeft = haybales[causeIndex] - radius
    searchRight = haybales[causeIndex] + radius
    # search left first
    pointer = causeIndex
    # to go smaller, reduce pointer by 1
    newThisRun = []
    while True:
        pointer -= 1
        if pointer < 0:
            break
        if haybales[pointer] < searchLeft:
            # WHOA, We're out of bounds.
            break
        # otherwise, just add the haybale.
        exploded.add(pointer)
        newThisRun.append(pointer)
    # reset pointer
    pointer = causeIndex
    while True:
        pointer += 1
        if pointer > len(haybales) - 1:
            # OUT OF BOUNDS
            break
        if haybales[pointer] > searchRight:
            break
        exploded.add(pointer)
        newThisRun.append(pointer)
        #print("exploded haybale " + str(haybales[pointer]) + "     at : " + str(pointer) + " because of " + str(haybales[causeIndex]) + " with radius " + str(radius))
    # now, simulate on EACH of the haybales.

    exExploded = set()
    for haybale in newThisRun:
        #if haybale == haybales[causeIndex]:
        #    continue # Whoa, let's not get into a loop here!
        if haybales[haybale] in treated or haybale in new:
            continue
        #print("Now simulating: " + str(haybale))
        newExploded = explodeHaybale(haybale, exploded.copy(), radius + 1, treated, newThisRun)
        treated.add(haybale)
        exExploded = newExploded | exExploded
    exploded = exExploded | exploded
    return exploded



f = open("angry.in")
haybalesCount = int(f.readline().strip())
haybales = []


for i in range(haybalesCount):
    haybales.append(int(f.readline().strip()))

# sort the haybales
haybales.sort()
maxx = -1
for shotHaybale in range(len(haybales)):
    # shot haybales will be the one that is shot.
    # simulate.
    a = explodeHaybale(shotHaybale, set(), 1, set(), [])
    print(a)
    e = len(a)
    if e > maxx:
        maxx = e
f = open("angry.out", "w")
f.write(str(maxx))
f.close()

# test data:
# haybales = [3,4,5,6,8,13]
# exploded: set.
# haybale: haybale to be exploded. (the index in the haybales list. )
# the range of how much these haybales are supposed to explode.
