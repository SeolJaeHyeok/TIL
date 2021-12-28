def pow(a, b, m):
    result = 1
    while b > 0:
        if b % 2 != 0:
            result = (result * a) % m
        b //= 2
        a = (a * a) % m

    return result

t = int(input())

mod = int(1e9) + 7
for _ in range(t):
    n = int(input())
    print(pow(2, n-2, mod))

