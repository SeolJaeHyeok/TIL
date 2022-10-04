def solution(brown, yellow):
    total = brown + yellow

    for i in range(1, total + 1):
        if total % i == 0:
            a = total // i
            if a >= i:
                if a * 2 + i * 2 == brown + 4:
                    return [a, i]

print(solution(10, 2))
print(solution(8, 1))
print(solution(24, 24))