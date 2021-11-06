def solution(n):
    answer = 0
    for i in range(1, n + 1):
        tmp = 0
        for j in range(i, n + 1):
            tmp += j
            if tmp == n:
                answer += 1
                break
            if tmp > n:
                break

    return answer


def solution(n):
    return len([i for i in range(1, n + 1, 2) if n % i == 0])