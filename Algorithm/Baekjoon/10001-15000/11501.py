# 주식
# 시간 초과, 그리디
# import sys
#
# t = int(sys.stdin.readline())
#
# for _ in range(t):
#     days = int(sys.stdin.readline())
#     array = list(map(int, sys.stdin.readline().split()))
#
#     profit = 0
#     for i in range(len(array) - 1):
#         tmp = 0
#         cur = array[i]
#         for j in range(i + 1, len(array)):
#             if cur >= array[j]:
#                 continue
#             else:
#                 tmp = max(tmp, array[j] - cur)
#         # print(tmp)
#         profit += tmp
#
#     print(profit)


# 2, 시간 초과
# import sys
#
# t = int(sys.stdin.readline())
#
# for _ in range(t):
#     days = int(sys.stdin.readline())
#     array = list(map(int, sys.stdin.readline().split()))
#
#     profit = 0
#     for i in range(len(array) - 1):
#         prev, next = i, i + 1
#         while True:
#             if next == len(array) - 1:
#                 break
#             if array[prev] > array[next]:
#                 break
#             elif array[prev] <= array[next]:
#                 # prev = next
#                 next += 1
#                 if array[prev] >= array[next]:
#                     next -= 1
#                     break
#
#         if array[prev] < array[next]:
#             profit += array[next] - array[prev]
#
#     print(profit)


# 3, 뒤에서부터 검색
import sys

t = int(sys.stdin.readline())

for _ in range(t):
    days = int(sys.stdin.readline())
    array = list(map(int, sys.stdin.readline().split()))

    # 맨 마지막 값을 최대값으로 지정하고
    max_price = array[-1]
    profit = 0
    # 마지막 바로 이전 값부터 왼쪽으로 순회
    for i in range(days - 2, -1, -1):
        # 최대값이 이전 값보다 작으면 최대값 갱신
        if max_price < array[i]:
            max_price = array[i]
        # 최대값이 이전 값보다 크면 이익 산출
        else:
            profit += max_price - array[i]

    print(profit)
