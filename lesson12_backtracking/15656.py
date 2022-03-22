n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
ans = [0]*m

def func(k):
	if k == m:
		print(*ans, sep=' ')
		return
	for i in range(n):
		ans[k] = arr[i]
		func(k+1)

func(0)