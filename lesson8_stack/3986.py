n = int(input())
count = 0
for _ in range(n):
    s = input()
    sto = []
    for st in s:
        if not sto or sto[-1] != st:
            sto.append(st)
        elif sto[-1] == st:
            sto.pop()
    if not sto:
        count += 1
print(count)