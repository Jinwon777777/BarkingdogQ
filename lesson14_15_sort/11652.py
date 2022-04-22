import sys
### dictionary 사용이유는 key에 카드번호, value에 카드 갯수를 저장하여 값 세는 것을 편하게 해주고 sort도 편하게 해주기 위함
n = int(sys.stdin.readline())
num_dict = {}
card_val = set()
for _ in range(n):
	num = int(sys.stdin.readline())
	if num in card_val:
		num_dict[num] += 1
	else:
		num_dict[num] = 1
		card_val.add(num)
num_dict = sorted(num_dict.items())
### num_dict = sorted(num_dict.items(), key= lambda x : (-x[1],x[0])
ans = [0,0]
for k, v in num_dict:
	if v > ans[1]:
		ans[0] = k
		ans[1] = v
print(ans[0])