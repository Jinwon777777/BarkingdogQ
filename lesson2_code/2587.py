val = []
for _ in range(5):
    val.append(int(input()))
val.sort()
print(int(sum(val) / 5))
print(val[2])