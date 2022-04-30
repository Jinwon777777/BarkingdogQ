n = int(input())

arr = [0]*(n+1)
road = [[0] for _ in range(n+1)]
road[1] = [1]

for i in range(2, n+1):
	arr[i] = arr[i-1] + 1
	road[i] = road[i-1] + [i]
	if i%2 == 0 and arr[i//2] + 1 < arr[i]:
		arr[i] = arr[i//2] + 1
		road[i] = road[i//2] + [i]
	if i%3 == 0 and arr[i//3] + 1 < arr[i]:
		arr[i] = arr[i//3] + 1
		road[i] = road[i//3] + [i]
print(arr[n])
road[n].sort(reverse=True)
print(*road[n], sep = ' ')
