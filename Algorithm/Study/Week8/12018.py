# 정렬을 이용하여 우선 순위 큐로 만들기 - 예외 처리가 부족해서 실패
n, m = map(int, input().split())

array = []
for i in range(n):
    p, l = map(int, input().split())
    board = list(map(int, input().split()))
    board.sort()
    array.append((p, l, board))

array.sort(key=lambda x: x[0])

count = 0
for arr in array:
    p, l, board = arr
    if p - l < 0:
        if m - 1 < 0:
            continue
        m -= 1
    else:
        if board[p-l] < 36:
            if m - board[p-l] < 0:
                continue
            m -= board[p - l]
        else:
            if m - 36 < 0:
                continue
            m -= 36

    count += 1

print(count)


# heapq 이용
import heapq

n, m = map(int, input().split())
q = []

for i in range(n):
    p, l = map(int, input().split())
    board = list(map(int, input().split()))
    board.sort()

    if p - l < 0: # 수강 가능 인원보다 수강 신청 인원이 적은 경우 최소한의 마일리지 사용
        heapq.heappush(q, 1)
    else: # 그렇지 않다면 마지막 순위를 가진 학생의 마일리지만큼 사용, 마일리지가 같을 경우 성준이에게 우선순위가 있기 때문에
        heapq.heappush(q, board[p-l])

m_sum = count = 0
for i in range(len(q)):
    m_sum += heapq.heappop(q)
    if m_sum <= m:
        count += 1
    else:
        break

print(count)
