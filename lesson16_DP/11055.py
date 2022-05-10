import sys
n = int(sys.stdin.readline())
num_arr = list(map(int, sys.stdin.readline().split()))

## 현재 값 저장 -> 더 큰 수를 만나면 저장 or 패스를 할 수 있음. 즉, 분기 발생
## 해당 분기를 저장해야 할 듯.
### 메모리 초과

## 무작정 추가하는게 답이 아닌듯..?
### 값이 1000까지 있기 때문에 array로 만들어버리기
check_arr = [0]*1001
for val in num_arr:
	check_arr[val] = max(check_arr[:val]) + val

print(max(check_arr))