N = int(input(""))
dat = list(map(int, input("").strip().split()))

def average(start, end):
    portion = dat[start:end + 1]
    ans = sum(portion)
    ans /= len(portion)
    return ans

ans = 0

for start in range(len(dat)):
    for end in range(len(dat)):
        if end < start: continue
        portion = dat[start:end + 1]
        avg = average(start, end)

        if avg in portion:
            ans += 1

print(ans)