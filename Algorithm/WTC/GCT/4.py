# sol
def solution(estimates, k):
    d = [0] * (len(estimates) - k + 1) # dp 테이블 선언
    d[0] = sum(estimates[0:k]) # 1번째부터 k번째까지 수의 합

    for i in range(1, len(d)):
        # 이전까지의 값에서 접속자 수의 가장 처음 값을 빼고 마지막 날 접속자 수를 더함
        d[i] = d[i - 1] - estimates[i - 1] + estimates[k]
        k += 1 # 마지막 날 증가

    return max(d)


print(solution([5, 1, 9, 8, 10, 5], 3))
print(solution([10, 1, 10, 1, 1, 4, 3, 10], 6))
print(solution([1, 1, 1, 1, 1, 3, 2, 1, 1, 1], 7))