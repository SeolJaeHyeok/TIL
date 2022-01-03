# 1, 시간 초과
import sys
input = sys.stdin.readline

n = int(input())
costs = list(map(int, input().split()))
max_cost = int(input())
costs.sort()


if sum(costs) <= max_cost:
    print(max(costs))
else:
    start = costs[0]
    end = costs[-1]
    mid = (start + end) // 2
    while True:
        answer = []
        for i in range(len(costs)):
            if costs[i] >= mid:
                answer.append(mid)
            else:
                answer.append(costs[i])

        if sum(answer) > max_cost:
            mid -= 1
        else:
            break

    print(max(answer))

# 2, Sol
import sys
input = sys.stdin.readline

n = int(input())
costs = list(map(int, input().split()))
max_cost = int(input())

# 예산 요청 합계가 정부 총 예산보다 작을 경우
if sum(costs) <= max_cost:
    print(max(costs))
else: # 그렇지 않을 경우
    start = 0
    end = max(costs)
    while start <= end:
        total = 0
        mid = (start + end) // 2 # 상한액
        # 상한액에 따라 총 비용 계산
        for cost in costs:
            if cost >= mid:
                total += mid
            else:
                total += cost

        # 계산한 비용이 정부 예산보다 많을 경우 상한액 줄이기
        if total > max_cost:
            end = mid - 1
        else: # 그렇지 않으면 상한액 늘리기
            start = mid + 1

    # 상한액 출력
    print(end)
