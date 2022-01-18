from collections import deque

ans = deque([])
count = 0

x, y = map(int, input().split())
comp = list(map(int, input().split()))

for i in range(1, x + 1):
    ans.append(i)
def count_left(ans, val):
    n = 0
    for i in range(len(ans) + 1):
        if ans[i] == val:
            n = i
            return n
def count_right(ans, val):
    n = 0
    for i in range(len(ans)-1, -1, -1):
        n += 1
        if ans[i] == val:
            return n
def deque_left(ans, left):
    for _ in range(left):
        ans.append(ans.popleft())
def deque_right(ans, right):
    ans.rotate(right)

for val in comp:
    if val != ans[0]:
        left = count_left(ans, val)
        right = count_right(ans, val)
        if left > right:
            count += right
            deque_right(ans, right)
        else:
            count += left
            deque_left(ans, left)
    ans.popleft()
print(count)