from sys import stdin
n = int(stdin.readline())
arr = [list(stdin.readline()) for _ in range(n)]

ans = []
def recursive(n, x, y):
	global ans
	start = arr[x][y]
	check = False
	for i in range(n):
		for j in range(n):
			if arr[x+i][y+j] != start:
				check = True
				ans.append('(')
				recursive(n//2, x,y)
				recursive(n//2, x, y+n//2)
				recursive(n//2, x+n//2, y)
				recursive(n//2, n//2+x, n//2+y)
				ans.append(')')
				break
		if check == True:
			break
	if check == False:
		ans.append(start)
recursive(n, 0, 0)
print(*ans, sep='')