inp = list(map(int, input("").strip().split()))
done = False
for indA in range(len(inp)):
    for indB in range(len(inp)):
        if indA == indB: continue
        for indC in range(len(inp)):
            if indA == indC or indB == indC: continue
            A = inp[indA]
            B = inp[indB]
            C = inp[indC]

            other4 = [A + B, B + C, C + A, A + B + C]
            other4ForThis = list(inp)
            other4ForThis.remove(A)
            other4ForThis.remove(B)
            other4ForThis.remove(C)
            other4.sort()
            other4ForThis.sort()
            if other4 == other4ForThis and A <= B and B <= C:
                ans = [A, B, C]
                done = True
                break
        if done:
            break
    if done:
        break

print(str(ans[0]) + " " + str(ans[1]) + " " + str(ans[2]))

