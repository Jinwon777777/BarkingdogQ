n = int(input())
a = [0] * 2000001
for h in list(map(int, input().split())):
    a[h] += 1
x = int(input())

ans = 0
for i in range(1, (x + 1) // 2):
    if a[i] == 1 and a[x - i] == 1:
        ans += 1

print(ans)