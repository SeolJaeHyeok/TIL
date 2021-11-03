# 단순 계산
def solution(left, right):
    answer = 0
    for i in range(left, right + 1):
        count = 0
        for j in range(1, i + 1):
            if i % j == 0:
                count += 1
        if count % 2 == 0:
            answer += i
        else:
            answer -= i
    return answer


# 최적화
import math

def solution(left, right):
    answer = 0
    for i in range(left, right + 1, 1):
        sqrt = math.sqrt(i)
        if int(sqrt) == sqrt:
            answer -= i
        else:
            answer += i

    return answer