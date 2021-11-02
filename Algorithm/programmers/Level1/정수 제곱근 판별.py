def solution(n):
    a = 1
    while True:
        if a > n:
            break
        if n == a * a:
            return (a + 1) ** 2
        a += 1

    return -1