### 최소의 칸수이기 때문에 BFS 사용
from collections import deque
n, m = map(int, input().split())

maze = [list(map(int, input())) for _ in range(n)]

arr = deque([])
visited = [[False]*m for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

arr.append((0,0,1))
visited[0][0] = True
while arr:
    x, y, cnt = arr.popleft()
    if (x, y) == (n-1, m-1):
        print(cnt)
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m: 
            if maze[nx][ny] == 1 and visited[nx][ny] == False:
                arr.append((nx, ny, cnt+1))
                visited[nx][ny] = True