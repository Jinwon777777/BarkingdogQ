from collections import deque
n = int(input())
arr = [list(input()) for _ in range(n)]
visited = [[False]*n for _ in range(n)]
a_cnt = 0
b_cnt = 0
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def bfs(i:int, j:int, v:bool):
	q = deque([])
	q.append((i,j))
	visited[i][j] = True
	while q:
		x, y = q.popleft()
		z = arr[x][y]
		for k in range(4):
			nx = x + dx[k]
			ny = y + dy[k]
			if (0<= nx < n) and (0<= ny < n) and not visited[nx][ny]:
				if z == arr[nx][ny]:
					q.append((nx, ny))
					visited[nx][ny] = True
				elif not v and (z in ('R', 'G') and arr[nx][ny] in ('R', 'G')):
					q.append((nx, ny))
					visited[nx][ny] = True					


for i in range(n):
	for j in range(n):
		if visited[i][j] == False:
			bfs(i, j, True)
			a_cnt+=1
visited = [[False]*n for _ in range(n)]
for i in range(n):
	for j in range(n):
		if visited[i][j] == False:
			bfs(i, j, False)
			b_cnt+=1
print(a_cnt, b_cnt)