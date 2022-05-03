n = int(input())

if n == 1:
	print(1)
elif n == 2:
	print(3)
else:
	dp = [0]*(n+1)
	dp[1] = 1
	dp[2] = 3
	'''
	3은 1 + 2 and 2 + 1
	4는 2 + 2 and 3 + 1
	'''
	for i in range(3, n+1):
		dp[i] = (dp[i-1] + dp[i-2]*2)%10007
	print(dp[n])