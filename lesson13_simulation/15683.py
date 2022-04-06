import sys
from copy import deepcopy

n,m = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
cctv_arr = []
zero_cnt = n*m + 1
move = [[], 
[[0],[1],[2],[3]],
[[0,2], [1,3]],
[[2,3],[1,2],[0,1],[3,0]],
[[0,1,2],[1,2,3],[2,3,0],[3,0,1]],
[[0,1,2,3]]]
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

for i in range(n):
	for j in range(m):
		if arr[i][j] != 6 and arr[i][j] != 0:
			cctv_arr.append((i, j, arr[i][j]))

def zero_count(arr):
	cnt = 0
	for i in range(n):
		for j in range(m):
			if arr[i][j] == 0:
				cnt+=1
	return cnt

def dfs(depth, arr):
	global zero_cnt
	if depth == len(cctv_arr):
		cnt = zero_count(arr)
		zero_cnt = min(cnt, zero_cnt)
		return
	tmp = deepcopy(arr)
	x,y,v = cctv_arr[depth]
	for com in move[v]:
		for val in com:
			nx = x
			ny = y
			while True:
				nx += dx[val]
				ny += dy[val]
				if nx >= 0 and nx < n and ny >= 0 and ny < m and tmp[nx][ny] != 6:
					if tmp[nx][ny] == 0:
						tmp[nx][ny] = 7
				else:
					break
		dfs(depth+1, tmp)
		tmp = deepcopy(arr)
dfs(0, arr)
print(zero_cnt)