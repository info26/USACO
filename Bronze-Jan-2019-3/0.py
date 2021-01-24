f = open("guess.in", "r")
guessPossibilties = int(f.readline())
data = []
charToAnimal = {}
animals = []
for i in range(guessPossibilties):
    temp = f.readline().strip().split(" ")
    data.append(
        [
            temp[0],
            temp[2:2 + int(temp[1])]
        ]
    )
    animals.append( temp[0] )
    for i in temp[2: 2 + int(temp[1])]:
        if i in charToAnimal:
            charToAnimal[i].append( temp[0] )
        else:
            charToAnimal[i] = [temp[0]]
f.close()

maxx = 0

for animal in data:
    # assume animal is the one bessie thought of. 
    yesses = 0
    plausibleAnimals = set( animals )
    animal[1].sort(key=lambda x: len(charToAnimal[x]))
    maxNumber = 0
    maxAnimal = None
    for i in data:
        if i[0] == animal[0]:
            continue
        richness = len( set(animal[1]) & set(i[1]) )
        if richness > maxNumber:
            maxNumber = richness
            maxAnimal = i
    yesses = maxNumber
    if yesses > maxx:
        maxx = yesses


f = open("guess.out", "w")
f.write( str( maxx+1 ) + "\n")
f.close()