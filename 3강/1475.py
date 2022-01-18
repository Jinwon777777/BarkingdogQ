n = int(input())
ans = [0] * 10
while n > 0:
    ans[n % 10] += 1
    n = n // 10

if (ans[6] + ans[9]) % 2 == 1:
    x = (ans[6] + ans[9]) // 2 + 1
else:
    x = (ans[6] + ans[9]) // 2
ans[6] = ans[9] = x
print(max(ans))