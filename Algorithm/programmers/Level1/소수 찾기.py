# 시간 초과, 56.3/100
def solution(n):
    answer = 0
    for i in range(2, n + 1):
        count = 0  # 각 수의 약수의 개수
        # n / 2 만큼까지 순회
        for j in range(1, i + 1 // 2):
            if i % j == 0:
                count += 1
        count += 1  # 자기 자신은 언제나 자신의 약수이므로 1 추가
        # 약수의 개수가 2개이면 결과 값에 추가
        if count == 2:
            answer += 1

    return answer

# 시간 초과
def solution(n):
    count = 0
    for num in range(2, n + 1):
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            count += 1

    return count

# 에라토스테네스의 체, sol
def solution(n):
    num = set(range(2, n + 1))

    for i in range(2, n + 1):
        if i in num:
            num -= set(range(2 * i, n + 1, i))

    return len(num)