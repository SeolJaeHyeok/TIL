# 1로 만들기
# my
input_data = int(input())


def solution(x):
    count = 0
    while x != 1:
        # 가능한 큰 수로 나누어 떨어지는 경우부터 차례대로 검사
        # 5로 나누어 떨어지는 경우
        if x % 5 == 0:
            x /= 5
        else:  # 5로 나누어 떨어지지 않는 경우에서
            # 1을 뺏을 때 5로 나누어 떨어지는 경우
            if (x - 1) % 5 == 0:
                x -= 1
            # 그렇지 않고 3으로 나누어 떨어지는 경우
            elif x % 3 == 0:
                x /= 3
            # 5와 3으로 나누어 떨어지지 않고 2로 나누어 떨어지는 경우
            elif x % 2 == 0:
                x /= 2
            # 2,3,5 모두와 나누어 떨어지지 않는 경우
            else:
                x -= 1
        count += 1

    return count


print(solution(input_data))


# sol
# 정수 X를 입력 받기
x = int(input())

# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [0] * 1000001

# 다이나믹 프로그래밍(Dynamic Programming) 진행(보텀업)
for i in range(2, x + 1):
    # 현재의 수에서 1을 빼는 경우
    d[i] = d[i - 1] + 1
    # 현재의 수가 2로 나누어 떨어지는 경우
    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)
    # 현재의 수가 3으로 나누어 떨어지는 경우
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)
    # 현재의 수가 5로 나누어 떨어지는 경우
    if i % 5 == 0:
        d[i] = min(d[i], d[i // 5] + 1)

print(d[x])
