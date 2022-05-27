t, w = map(int, input().split())

# 값을 받아오면 비교를 해야함
# 점화식을 어떻게 해야하지?
# 시간, 움직인 횟수를 사용한 표 만들기
dp = [[0]*(w+1) for _ in range(t)]

plum = []
for _ in range(t):
	plum.append(int(input()))

for i in range(t):
	if i == 0:
		dp[i][plum[i] - 1] = 1
		continue
	for j in range(w+1):
		# 움직임이 없는경우 전 것의 것에 1 더하거나 더하지 않거나
		if j == 0:
			if plum[i] == 1:
				dp[i][0] = dp[i-1][0] + 1
			else:
				dp[i][0] = dp[i-1][0]
		else:
			if j%2 == 0 and plum[i] == 1:
				dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + 1
			elif j%2 == 1 and plum[i] == 2:
				dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + 1
			else:
				dp[i][j] = max(dp[i-1][j-1], dp[i-1][j])
print(max(dp[t-1]))