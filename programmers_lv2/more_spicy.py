### heap 사용
""" import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while scoville[0] < K:
        if len(scoville) == 1:
            return (-1)
        val = heapq.heappop(scoville) + heapq.heappop(scoville)*2
        heapq.heappush(scoville, val)
        answer+=1
    return answer
 """
### deque만 사용
from collections import deque
def solution(scoville, K):
    answer = 0
    scoville.sort()
    a = deque(scoville)
    b = deque([])
    while (a and a[0] < K) or (b and b[0] < K):
        if len(a) + len(b) <= 1:
            return(-1)
        x = []
        for i in range(2):
            if a and b:
                if a[0] >= b[0]:
                    x.append(b.popleft())
                else:
                    x.append(a.popleft())
            elif a:
                x.append(a.popleft())
            else:
                x.append(b.popleft())
        b.append(x[0] + 2*x[1])
        answer+=1
    return answer