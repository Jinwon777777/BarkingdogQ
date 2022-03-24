import sys
arr = [list(sys.stdin.readline().rstrip()) for _ in range(5)]
delta = [(-1,0), (1,0), (0,-1), (0,1)]
ans = set()

### 좀 더 머리를 말랑말랑하게 하기
def backtrack(ans_list, cnt=0, s_cnt=0, y_cnt=0):
	if y_cnt > 3:
		return
	# 그냥 시작점을 S인곳으로만 설정하고 시작했기 때문에
	if cnt == 6:
		ans_list.sort()
		ans.add(tuple(ans_list))
	else:
		adj = []
		for com in range(len(ans_list)):
			for i in range(4):
				dx = ans_list[com][0] + delta[i][0]
				dy = ans_list[com][1] + delta[i][1]
				if dx < 0 or dx >=5 or dy < 0 or dy >=5:
					continue
				if (dx, dy) in ans_list:
					continue
				adj.append((dx,dy))
		for adjacent in adj:
			nx, ny = adjacent
			if arr[nx][ny] == 'S':
				backtrack(ans_list+[(nx,ny)], cnt+1, s_cnt+1, y_cnt)
			else:
				backtrack(ans_list+[(nx,ny)], cnt+1, s_cnt, y_cnt+1)

for i in range(5):
	for j in range(5):
		if arr[i][j] == 'S':
			backtrack([(i,j)], cnt=0, s_cnt=1)
print(len(ans))