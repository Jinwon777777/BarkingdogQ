from collections import deque

n, m = map(int, input().split())
arr = []
cnt = 0
max_cnt = 0
visited = [[False]* m for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def bfs(x, y):
    this_cnt = 1
    que = deque([])
    que.append((x, y))
    visited[x][y] = True
    while que:
        x, y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if arr[nx][ny] == 1 and visited[nx][ny] == False:
                    visited[nx][ny] = True
                    que.append((nx, ny))
                    this_cnt += 1
    return this_cnt

for _ in range(n):
    arr.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        if arr[i][j] == 1 and visited[i][j] == False:
            cnt += 1
            max_cnt = max(bfs(i, j), max_cnt)

print(cnt)
print(max_cnt)