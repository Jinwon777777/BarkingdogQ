import sys

n = int(sys.stdin.readline())
arr = [sys.stdin.readline().rstrip() for _ in range(n)]

def num_sum(s:str) -> int:
	result = 0
	for c in s:
		if c.isdigit():
			result += int(c)
	return result

arr.sort(key=lambda x : (len(x), num_sum(x), x))
print(*arr, sep='\n')