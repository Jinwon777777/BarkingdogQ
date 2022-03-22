n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
visited = [False]*n
ans = []

def func(k):
	if k == m:
		print(*ans, sep=' ')
		return
	check = 0
	# check를 통해 중복 검증 가능
	for i in range(n):
		if not visited[i] and check != arr[i]:
			visited[i] = True
			ans.append(arr[i])
			check = arr[i]
			func(k+1)
			visited[i] = False
			ans.pop()
func(0)