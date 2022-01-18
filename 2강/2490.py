ans = ['E', 'A', 'B', 'C', 'D']
for _ in range(3):
    a = list(map(int, input().split()))
    x = a.count(0)
    print(ans[x])