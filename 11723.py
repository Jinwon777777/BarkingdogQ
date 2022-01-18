import sys
n = int(input())
s = set()
    
for j in range(n):
    c = list(sys.stdin.readline().strip().split())
    if len(c) == 1:
        if c[0] == 'clear':
            s = set()
        else:
            s = set([i for i in range(1,21)])
        continue

    c1 = c[0]
    c2 = int(c[1])
    if c1 == 'add':
        s.add(c2)
    elif c1 == 'remove':
        s.discard(c2)
    elif c1 == 'check':
        print(1 if c2 in s else 0)
    elif c1 == 'toggle':
        if c2 in s:
            s.discard(c2)
        else:
            s.add(c2)