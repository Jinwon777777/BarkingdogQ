from sys import stdin
n = int(stdin.readline())
for _ in range(n):
	a_num, b_num = map(int, stdin.readline().split())
	a_lst = list(map(int, stdin.readline().split()))
	b_lst = list(map(int, stdin.readline().split()))
	a_lst.sort()
	b_lst.sort()
	b_idx = 0
	cnt = 0
	for a_idx in range(a_num):
		while True:
			if b_idx == b_num or b_lst[b_idx] >= a_lst[a_idx]:
				break
			b_idx+=1
		cnt += b_idx
	print(cnt)