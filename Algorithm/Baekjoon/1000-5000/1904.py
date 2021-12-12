# 01타일
n = int(input())
d = [0] * 1000001

d[1] = 1
d[2] = 2
for i in range(3, n + 1):
    d[i] = (d[i - 2] + d[i - 1]) % 15746

print(d[n])
