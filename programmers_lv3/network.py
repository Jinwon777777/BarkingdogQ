from collections import deque
def solution(n, computers):
    q = deque([])
    q.append(0)
    visited = [False]*n
    ntw_cnt = 1
    while q:
        x = q.popleft()
        visited[x] = True
        for i in range(n):
            if computers[x][i] == 1 and not visited[i]:
                q.append(i)
            elif i == n-1 and not q:
                for j in range(n):
                    if not visited[j]:
                        q.append(j)
                        ntw_cnt+=1
                        break
    return ntw_cnt
### dfs