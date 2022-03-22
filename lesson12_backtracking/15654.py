n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
ans = [0]*m
visited = [False]*n

def func(k):
	if k == m:
		print(*ans, sep=' ')
		return
	for i in range(n):
		if not visited[i]:
			ans[k] = arr[i]
			visited[i] = True
			func(k+1)
			visited[i] = False

func(0)