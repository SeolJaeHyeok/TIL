import sys
import math

input = sys.stdin.readline

n, m = map(int, input().split())
array = [int(input()) for _ in range(m)]

def binary_search(left, right):
    answer = 1e9
    while left <= right:
        mid = (left + right) // 2  # 가장 보석을 많이 가진 학생의 보석 개수
        students = 0  # mid만큼의 질투심(보석)을 가질 경우의 나눠 줄 수 있는 학생 수
        for i in array:
            students += math.ceil(i / mid)

        if students > n:
            left = mid + 1
        else:
            answer = min(answer, mid)
            right = mid - 1

    return answer

print(binary_search(1, max(array)))