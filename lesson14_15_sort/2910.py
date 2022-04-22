import sys
n, c = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
ans = []

num_dict = {}
for i in range(n):
	if arr[i] in num_dict:
		num_dict[arr[i]][0] += 1
	else:
		num_dict[arr[i]] = [1,i]

num_dict = sorted(num_dict.items(), key=lambda x : (-x[1][0], x[1][1]))
for v, l in num_dict:
	ans = ans + ([v]*l[0])
print(*ans, sep = ' ')