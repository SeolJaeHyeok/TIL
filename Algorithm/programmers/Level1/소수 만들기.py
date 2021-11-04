from itertools import combinations

def solution(nums):
    answer = 0
    comb = list(combinations(nums, 3))

    for a, b, c in comb:
        value = a + b + c
        for i in range(2, value // 2):
            if value % i == 0:
               break
        else:
            answer += 1

    return answer