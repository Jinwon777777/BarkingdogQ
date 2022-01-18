a = list(map(int, input().split()))

ct = [0] * 7

for h in a:
    ct[h] += 1

ans = 0
if max(ct) == 3:
    ans = 10000 + (ct.index(3) * 1000)
elif max(ct) == 2:
    ans = 1000 + (ct.index(2) * 100)
else:
    for i in range(6, 1, -1):
        if ct[i] == 1:
            ans = 100 * i
            break

print(ans)