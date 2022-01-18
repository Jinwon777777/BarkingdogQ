s = str(input())
ans = [0 for i in range(26)]
val = 0

for c in s:
    if c > 'Z':
        c = chr(ord(c) - 32)
    ans[ord(c) - 65] += 1

m = ans.index(max(ans))
for n in ans:
    if n == max(ans):
        val += 1
if val == 1:
    print(chr(m + 65))
else:
    print('?')