n = int(input())
m = int(input())

if n >= 2:
    d = [1] * (n+1)
    d[2] = 2
    for i in range(3, n+1):
        d[i] = d[i-1] + d[i-2]

    start = answer = 1
    for _ in range(m):
        vip = int(input())
        answer *= d[vip - start]
        start = vip + 1
    print(answer * d[n - start + 1])
else:
    for _ in range(m):
        vip = int(input())
    print(1)