#from collections import deque
import sys
s = str(sys.stdin.readline().strip())

tmp = []
count = 0
active = 0
for st in s:
    tmp.append(st)
    if st == '(':
        active += 1
    else:
        if tmp[-2] == ')':
            active -= 1
            count += 1
        else:
            active -= 1
            count += active

print(count)