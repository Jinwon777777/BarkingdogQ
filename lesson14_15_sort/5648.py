import sys
arr = []
arr = sys.stdin.readline().split()
n = int(arr.pop(0))
while len(arr) < n:
	tmp = sys.stdin.readline().split()
	arr = arr + tmp
ans = []
for val in arr:
	ans.append(int(val[::-1]))
ans.sort()
print(*ans)
