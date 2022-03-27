answer = 0
numbers = [1,1,1,1,1]
target=3

def backtracking(k:int, numbers, target, val:int):
	global answer
	if k==len(numbers):
		if val == target:
			answer+=1
		return
	for i in [1, -1]:
		val += i*numbers[k]
		backtracking(k+1, numbers, target, val)
		val -= i*numbers[k]

backtracking(0, numbers, target, 0)
print(answer)