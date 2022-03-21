n, r, c = map(int, input().split())

count = 0
def recursive(n, r, c):
	global count
	if n == 0:
		return 0
	if r >= 2**(n-1):
		r -= 2**(n-1)
		count += 2**(2*n-1)
	if c >= 2**(n-1):
		c -= 2**(n-1)
		count += 2**(2*n-2)
	recursive(n-1, r, c)
recursive(n, r, c)
print(count)