from collections import deque
import sys

n = int(sys.stdin.readline())
dx = [1, -1, 2, -2]
dy = [2, -2, 1, -1]
for _ in range(n):
	m = int(sys.stdin.readline())
	x1, y1 = map(int, sys.stdin.readline().split())
	x2, y2 = map(int, sys.stdin.readline().split())
	visited = [[False]*m for _ in range(m)]
	q = deque([])
	q.append([x1, y1, 0])
	visited[x1][y1] = True
	while q:
		x, y, t_cnt = q.popleft()
		if x == x2 and y == y2:
			print(t_cnt)
			break
		for i in range(8):
			nx = x + dx[i//2]
			if i > 3:
				ny = y + dy[2 + i%2]
			else:
				ny = y + dy[i%2]
			if 0<= nx < m and 0<= ny < m and visited[nx][ny] == False:
				q.append([nx, ny, t_cnt+1])
				visited[nx][ny] = True	