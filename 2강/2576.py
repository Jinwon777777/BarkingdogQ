ans = []
for _ in range(7):
    a = int(input())
    if (a % 2) == 1:
        ans.append(a)

if ans:
    print(sum(ans))
    print(min(ans))
else:
    print(-1)