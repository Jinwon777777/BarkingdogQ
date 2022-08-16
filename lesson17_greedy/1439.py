lst = list(map(int,list(input())))

check = lst[0]
cnt = 0
for val in lst:
	if val != check:
		cnt+=1
		check = val

print(cnt//2 + cnt%2)