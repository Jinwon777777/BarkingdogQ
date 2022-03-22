n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
ans = []

def func(k, l):
	if k == m:
		print(*ans, sep=' ')
		return
	check = 0
	# check를 통해 중복 검증 가능
	for i in range(l, n):
		if check != arr[i]:
			ans.append(arr[i])
			check = arr[i]
			func(k+1, i)
			ans.pop()
func(0, 0)