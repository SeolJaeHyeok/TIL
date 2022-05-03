import sys
import heapq
input = sys.stdin.readline

n = int(input())

array = []
for _ in range(n):
    x = int(input())
    min_val = 1e9

    if x != 0:
        # 절대값을 우선순위로 하는 우선순위 큐에 추가
        heapq.heappush(array, (abs(x), x))
        continue

    if x == 0:
        if len(array) == 0:
            print(0)
        else:
            # 절대값이 가장 작은 원소의 원래 값 출력
            print(heapq.heappop(array)[1])