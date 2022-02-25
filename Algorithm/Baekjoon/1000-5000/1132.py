import sys
from collections import defaultdict
# input = sys.stdin.readline

n = int(input())

# 각 알파벳의 계수 합치기
array = [[0, False] for _ in range(10)] # A, B, C, D ...
for _ in range(n):
    alpha = input().rstrip()
    array[ord(alpha[0]) - 65][1] = True # 첫 번째 알파벳 체크
    m = 1
    for i in range(len(alpha) - 1, -1, -1):
        # 각 알파벳에 맞는 인덱스에 더하기
        array[ord(alpha[i]) - 65][0] += m
        m *= 10

# 내림 차순 정렬
array.sort(reverse=True)

# 정렬 후 마지막 알파벳이 맨 앞에 존재하는 경우 맨 앞의 값으로 존재하지 않는 알파벳 하나를 제거
if array[-1][1]:
    for i in range(8, -1, -1):
        if not array[i][1]:
            del array[i]
            break

answer = 0
for i in range(9):
    answer += array[i][0] * (9 - i)

print(answer)