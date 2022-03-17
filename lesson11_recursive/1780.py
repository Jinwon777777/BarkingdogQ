import sys
n = int(sys.stdin.readline())

arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

n_1 = 0
n_2 = 0
n_3 = 0

def recursive(x, y, n):
	global n_1, n_2, n_3
	start = arr[x][y]
	div = n//3
	for i in range(x, x+n):
		for j in range(y, y+n):
			if arr[i][j] != start:
				for k in range(3):
					for l in range(3):
						recursive(x+k*div, y+l*div, div)
				return
	if start == -1:
		n_1+=1
	elif start == 0:
		n_2+=1
	elif start == 1:
		n_3+=1
recursive(0,0,n)
print(n_1, n_2, n_3, sep='\n')