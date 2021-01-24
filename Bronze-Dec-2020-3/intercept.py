N = int(input(""))
dat = []
for b in range(N):
    line = input("")
    line = line.split()
    dat.append({
        "dir": line[0],
        "x": int(line[1]),
        "y": int(line[2]),
        "id": b,
        "res": None
    })

ans = [99999999999] * N


NLines = []

firstIterData = list(filter(lambda cow: cow["dir"] == "N", dat))
firstIterData.sort(key=lambda x: x["x"])

for cow in firstIterData:
    NLines.append({
        "x": cow["x"], 
        "start": cow["y"], 
        "end": 99999999999, 
        "created_by": cow["id"]
    })

secondIterData = list(filter(lambda cow: cow["dir"] == "E", dat))
secondIterData.sort(key=lambda x: x["y"])

for cow in secondIterData:
    # beginning from the lowest first, let's challenge it against
    # each other cow. 

    for line in NLines:
        if cow["y"] < line["start"] or cow["y"] > line["end"]:
            continue
        if cow["x"] > line["x"]:
            continue
        # we have an actual interception!
        cowToHere = abs(cow["x"] - line["x"])
        lineToHere = abs(cow["y"] - line["start"])


        if lineToHere > cowToHere:
            # the cow wins!
            line["end"] = cow["y"]
        
        if lineToHere < cowToHere:
            # the cow lost. 
            # set the cow to end here. 
            cow["res"] = abs(cow["x"] - line["x"])
            break
        # if they are the same, well do nothing. 


for line in NLines:
    if line["end"] == 99999999999:
        dat[line["created_by"]]["res"] = "Infinity"
    else:
        dat[line["created_by"]]["res"] = abs(line["start"] - line["end"])

for cow in dat:
    if cow["res"] == None:
        cow["res"] = "Infinity"

for cow in dat:
    print(cow["res"])

