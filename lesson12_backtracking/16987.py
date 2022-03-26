import sys
n = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
ans = 0
def recursive(arr, k):
	global ans
	if k == n:
		count = 0
		for i in range(n):
			if arr[i][0] <=0:
				count+=1
		ans = max(ans, count)
		return
	if arr[k][0] <= 0:
		recursive(arr, k+1)
	else:
		# 더이상 깰 계란 있는지 체크하는 용도
		check = False
		for i in range(n):
			if i == k or arr[i][0]<=0:
				continue
			arr[k][0] -= arr[i][1]
			arr[i][0] -= arr[k][1]
			check = True
			recursive(arr,k+1)
			arr[k][0] += arr[i][1]
			arr[i][0] += arr[k][1]
		if not check:
			recursive(arr, k+1)
recursive(arr, 0)
print(ans)