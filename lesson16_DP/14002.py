n = int(input())
arr = list(map(int, input().split()))

dp = [0]*n
dp[0] = (arr[0], [arr[0]])

for i in range(1, n):
	max_n = arr[i]
	chk = -1
	for idx, v in enumerate(dp[:i]):
		if max_n < v:
			chk = idx
			max_n = v
	