import sys
from collections import deque

n = int(sys.stdin.readline())
flowerList = []

for _ in range(n):
	a,b,c,d = map(int, sys.stdin.readline().split())
	flowerList.append((a*100 + b, c*100 + d))

# 같은 날 시작하면 더 일찍 끝나는 꽃이 우선적으로 오게(걸러내야하니까)
flowerList = deque(sorted(flowerList, key= lambda x: (x[0], x[1])))

# 끝나는 날짜, 즉 이어받아져야하는 날
tDate = 301
# 최종적으로 꽃이 끝나는 날짜
end = 0
cnt = 0

while flowerList:
	if tDate >= 1201 or tDate < flowerList[0][0]:
		break
	for _ in range(len(flowerList)):
		# 제일 빨리 피는 친구와 이어져야 하니까, 지기 전에 펴야하니까
		if tDate >= flowerList[0][0]:
			if end <= flowerList[0][1]:
				end = flowerList[0][1]
			flowerList.popleft()
		# 이어지지 못하는 경우(즉 현재 꽃과 다음 꽃 사이 빈공간이 존재하는 경우)
		else:
			break
	tDate = end
	cnt+=1
if end < 1201:
	print(0)
else:
	print(cnt)
