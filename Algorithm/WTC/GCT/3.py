# sol
from itertools import combinations

def solution(arr, k, t):
    answer = 0
    for i in range(k, len(arr) + 1):
        # k개 이상 선택하는 모든 경우의 수
        tmp = list(combinations(arr, i))
        for j in tmp:
            # 각 경우의 수의 보장 금액의 합이 t 이하일 경우 카운팅
            if sum(j) <= t:
                answer += 1

    return answer

solution([2,5,3,8,1], 3, 11)
solution([1,1,2,2], 2, 3)
solution([1,2,3,2], 2, 2)