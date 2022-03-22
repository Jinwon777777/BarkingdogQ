n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
ans = [0]*m
visited = [False]*n

def func(k, l):
	if k == m:
		print(*ans, sep=' ')
		return
	for i in range(l, n):
		if not visited[i]:
			ans[k] = arr[i]
			visited[i] = True
			func(k+1, i)
			visited[i] = False

func(0, 0)