# 효율성 x
def solution(arr):
    answer = 0
    total = 1
    for i in arr:
        total *= i

    for i in range(max(arr), total + 1):
        count = 0
        for j in arr:
            if i % j == 0:
                count += 1

        if count == len(arr):
            answer = i
            break

    return answer

# 효율성 O
import math

def solution(arr):
    answer = arr[0]

    for num in arr:
        answer = num * answer // math.gcd(num, answer)

    return answer