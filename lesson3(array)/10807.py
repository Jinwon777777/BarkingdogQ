n = int(input())
a = [0] * 201
for h in list(map(int, input().split())):
    if h == 0:
        a[h] += 1
    elif (-1 <= h <= -100):
        a[-h] += 1
    else:
        a[h + 100] += 1

x = int(input())
if x < 0:
    print(a[-x])
elif x == 0:
    print(a[x])
else:
    print(a[x+100])