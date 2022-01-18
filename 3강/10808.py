s = str(input())
i = 0
ans = [0] * 26
while (i < len(s)):
    ans[ord(s[i]) - 97] += 1
    i += 1
for j in range(26):
    print(ans[j], end = ' ')