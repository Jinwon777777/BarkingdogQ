import sys
l, c = map(int, sys.stdin.readline().split())
arr = list(sys.stdin.readline().split())
arr.sort()
ans = [0]*l
vowel = ['a', 'e', 'i', 'o', 'u']
visited = [False]*c

### 문제 잘읽기. 문제는 분명히 모음 한개, 자음 두개 이상이라 적혀있었음.
def func(k, n):
	if k == l:
		vo = 0
		co = 0
		for com in ans:
			if com in vowel:
				vo+=1
			else:
				co+=1
		if vo >= 1 and co >= 2:
			print(*ans, sep='')
		return
	for i in range(n, c):
		if not visited[i]:
			ans[k] = arr[i]
			visited[i] = True
			func(k+1, i)
			visited[i] = False

check_v = False
for v in arr:
	if v in vowel:
		check_v = True
		break
if check_v:
	func(0, 0)