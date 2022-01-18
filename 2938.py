n = int(input())

s = n // 5
count = 0

while s >= 0:
    t = n - 5*s
    r = t // 3
    if t % 3 == 0:
        count = s + r
        break
    s -= 1

if count:
    print(count)
else:
    print(-1)