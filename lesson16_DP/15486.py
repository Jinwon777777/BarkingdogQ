from sys import stdin

n = int(input())
schedule = []
dp = [0]*(n+1)
for _ in range(n):
	x, y = map(int, stdin.readline().split())
	schedule.append([x,y])
max_num = 0

for i in range(n):
	max_num = max(max_num, dp[i])
	if i + schedule[i][0] > n:
		continue
	dp[i + schedule[i][0]] = max(max_num + schedule[i][1], dp[i+schedule[i][0]])
print(max(dp))