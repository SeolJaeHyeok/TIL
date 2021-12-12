n = int(input())

d = [0] * (abs(n) + 1)
if n != 0:
    d[0] = 0
    d[1] = 1
    for i in range(2, len(d)):
        d[i] = (d[i-1] + d[i-2]) % 1000000000

    if n == 0:
        print(0)
    elif n < 0:
        if n % 2 == 0:
            print(-1)
        else:
            print(1)
    else:
        print(1)
else:
    print(0)

print(d[abs(n)])
