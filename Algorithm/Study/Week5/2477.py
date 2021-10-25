# 참외밭
k = int(input())
array = []
for i in range(6):
    direction, length = map(int, input().split())
    array.append((direction, length))

# 총 면적 계산
total = 0
max_horizon = max_vertical = max_horizon_idx = max_vertical_idx = 0
for i in range(len(array)):
    # 가로(동,서) 길이의 최대값과 해당 값의 인덱스 구하기
    if array[i][0] == 1 or array[i][0] == 2:
        if array[i][1] > max_horizon:
            max_horizon = array[i][1]
            max_horizon_idx = i
    else: # 세로(남,북) 길이의 최대값과 해당 값의 인덱스 구하기
        if array[i][1] > max_vertical:
            max_vertical = array[i][1]
            max_vertical_idx = i

# 큰 사각형의 넓이
total = max_horizon * max_vertical
# 부분 사각형의 가로, 세로 길이 -> 가장 큰 변을 기준으로 양 옆 변의 길이의 차이
width = abs(array[(max_horizon_idx + 1) % 6][1] - array[(max_horizon_idx - 1) % 6][1])
height = abs(array[(max_vertical_idx + 1) % 6][1] - array[(max_vertical_idx - 1) % 6][1])
# 큰 사각형에서 부분 사각형 뺴기
result = total - (width * height)
print(result * k)

"""
큰 사각형의 넓이를 구하고 작은 사각형의 넓이를 빼주는 방식으로 구현
육각형을 이루고 있고 반시계 방향으로 회전하면서 다시 원점으로 돌아온다고 했으니 원형 연결 리스트로 생각할 수 있다. 
- 먼저 가로, 세로 각각 가장 큰 변의 길이를 구한다. 입력받은 가로와 세로 길이 중 가장 큰 값이 큰 사각형의 가로, 세로 변의 길이다. 
- 해당 변의 위치를 기준으로 양 옆에 있는 두 변(가장 큰 변의 인덱스 +1, -1)의 차이가 작은 사각형의 가로, 세로 길이가 된다. 
"""







