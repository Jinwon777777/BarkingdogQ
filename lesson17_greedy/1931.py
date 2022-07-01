import sys

n = int(input())
confList = []
for _ in range(n):
	confList.append(tuple(map(int, sys.stdin.readline().split())))

confList.sort(key= lambda x: (x[1], x[0]))
cnt = 0
chk = 0

for val in confList:
	if val[0] >= chk:
		cnt+=1
		chk = val[1]
print(cnt)