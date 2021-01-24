f = open("blist.in")
numCows = int(f.readline())
timings = []
for i in range(numCows):
    timings.append(
        list(map(int, f.readline().strip().split()))
    )
f.close()
# ===================================================
events = []

for timing in timings:
    events.append(
        {"time": timing[0], "bucketDelta": timing[2]}
    )
    events.append(
        {"time": timing[1], "bucketDelta": -1 * timing[2]}
    )

events.sort(key=lambda d: d["time"]) # sort by the time

maxBuckets = -5
buckets = 0
for i in events:
    buckets += i["bucketDelta"]
    if buckets > maxBuckets:
        maxBuckets = buckets


f = open("blist.out", "w")
f.write(str(maxBuckets) + "\n")
f.close()