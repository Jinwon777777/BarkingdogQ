n = int(input())
lst = []
cnt = 0

for _ in range(n):
	lst.append(int(input()))

val = lst.pop()
while lst:
	if val <= lst[-1]:
		cnt += lst[-1] - val + 1
		lst[-1] = val - 1
	val = lst.pop()
print(cnt)