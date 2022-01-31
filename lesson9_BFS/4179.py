import sys
from collections import deque
r, c = map(int, sys.stdin.readline().split())
arr = deque([])
maze = [list(sys.stdin.readline()) for _ in range(r)]
visited = [[False]*c for _ in range(r)]
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
escape = False
left = 1

for i in range(r):
	for j in range(c):
		if maze[i][j] == 'J':
			### 지훈 위치는 3번째 탈출시간
			arr.appendleft((i, j, 0))
		elif maze[i][j] == 'F':
			### 불 위치는 3번째 -1
			arr.append((i, j, -1))

while arr:
	x, y, cnt = arr.popleft()
	if cnt != -1:
		if maze[x][y] == 'F':
			continue
		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]
			if nx < 0 or nx >= r or ny <0 or ny >= c:
				escape = True
				cnt+=1
				break
			elif maze[nx][ny] == '.' and visited[nx][ny] == False:
				visited[nx][ny] = True
				arr.append((nx, ny, cnt+1))
				maze[nx][ny] = 'J'
				left+=1
		maze[x][y] = '.'
		left -= 1
		if escape == True:
			print(cnt)
			break
	else:
		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]
			if 0 <= nx < r and 0 <= ny < c:
				if maze[nx][ny] == '.':
					arr.append((nx, ny, -1))
					maze[nx][ny] = 'F'
				elif maze[nx][ny] == 'J':
					left -= 1
					arr.append((nx, ny, -1))
					maze[nx][ny] = 'F'
					if left == 0:
						break
	if left == 0:
		print("IMPOSSIBLE")
		break

'''
다른 풀이 : 불 먼저 퍼뜨린 후 걸리는 시간을 map에 기록 (칸 마다 불이 퍼지는 게 몇초 후인지 기록) -> 비교해가면서 움직여가며 탈출
https://philipbox.tistory.com/30 참고
'''