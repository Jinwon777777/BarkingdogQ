from collections import deque
def solution(priorities, location):
    answer = 0
    arr = deque(priorities)
    for i in range(len(priorities)):
        x = arr.popleft()
        arr.append((x,i))
    while arr:
        check = True
        x, y = arr.popleft()
        for j in range(len(arr)):
            if x < arr[j][0]:
                check = False
                break
        if check:
            answer+=1
            if y == location:
                return answer
        else:
            arr.append((x, y))
    return answer