import sys
n, m = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))
arr = [0]
val = 0
for com in lst:
	val += com
	arr.append(val)

for _ in range(m):
	i, j = map(int, sys.stdin.readline().split())
	print(arr[j] - arr[i-1])
### 메모리 초과
'''
	if arr[i][j] != 0:
		print(arr[i][j])
	else:
		check = False
		for x in range(i, j+1):
			for y in range(j, x-1, -1):
				if arr[x][y] != 0:
					check = True
					arr[i][j] = arr[x][y] + sum(lst[i-1:x-1]) + sum(lst[y-1:j])
		if check == False:
			arr[i][j] = sum(lst[i-1:j])
		print(arr[i][j])
'''