"""
n개의 정수가 입력으로 주어지고,
이 중 연속한 부분 수열에 속한 원소들의 합이 최대가 될 때의 값을 출력하는 코드를 작성해보세요.
(단, 부분 수열은 최소 한 개 이상의 원소를 포함합니다.)

Input
7                           2
4 -1 2 -19 3 6 9            -2 -1

Output
18                          -1
"""
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

d = [0] * n

d[0] = arr[0]

for i in range(1, n):
    d[i] = max(d[i - 1] + arr[i], arr[i])

print(max(d))