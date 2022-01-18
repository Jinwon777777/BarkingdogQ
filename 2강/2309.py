a = []
for _ in range(9):
    a.append(int(input()))
count = sum(a)
a.sort()

x = -1
y = -1
for i in range(8):
    for j in range(i, 9):
        if (count - a[i] - a[j]) == 100:
            x = i
            y = j
            break
    if x != -1:
        break

for index, val in enumerate(a):
    if (index == x) or (index == y):
        continue
    print(val)