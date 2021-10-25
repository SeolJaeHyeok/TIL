# 화살표 그리기
import sys

n = int(sys.stdin.readline())
array = []
for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    array.append((x, y))

array.sort()

total = 0
for i in range(len(array)):
    location, color = array[i]
    leftValue = rightValue = 1e9

    # 출발점 기준 왼쪽 탐색
    left_idx = i - 1
    while left_idx >= 0:
        # 점점 왼쪽으로 탐색 중 색깔이 같은 점을 만나면
        if array[left_idx][1] == color:
            # 출발점과 왼쪽 점 사이의 거리 구하고 반복문 탈출
            leftValue = abs(array[i][0] - array[left_idx][0])
            break
        # 만나지 못하면 왼쪽으로 이동
        else:
            left_idx -= 1

    # 출발점 기준 오른쪽 탐색
    right_idx = i + 1
    while right_idx < n:
        # 점점 오른쪽으로 탐색 중 색깔이 같은 점을 만나면
        if array[right_idx][1] == color:
            # 출발점과 오른쪽 점 사이의 거리 구하고 반복문 탈출
            rightValue = abs(array[right_idx][0] - array[i][0])
            break
        # 만나지 못하면 오른쪽으로 이동
        else:
            right_idx += 1
    # 왼쪽과 오른쪽 중 더 작은 값 더하기
    total += min(leftValue, rightValue)

print(total)