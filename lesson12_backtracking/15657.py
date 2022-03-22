n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
ans = [0]*m

def func(k, l):
	if k == m:
		print(*ans, sep=' ')
		return
	for i in range(l, n):
		ans[k] = arr[i]
		func(k+1, i)

func(0, 0)