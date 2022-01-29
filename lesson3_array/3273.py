s = int(input())
l = list(map(int, input().split()))
l.sort()
v = int(input())
count = 0

for i in range(s - 1):
    x = v - l[i]
    if x <= 0:
        continue
    for j in range(i+1, s):
        if x == l[j]:
            count += 1
        elif x < l[j]:
            break
print(count)