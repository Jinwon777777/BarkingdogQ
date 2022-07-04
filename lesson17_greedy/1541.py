rawinput = input().split('-')
num = []

for val in rawinput:
	cnt = 0
	n = val.split('+')
	for v in n:
		cnt+=int(v)
	num.append(cnt)
reVal = num.pop(0)
for val in num:
	reVal -= val
print(reVal)