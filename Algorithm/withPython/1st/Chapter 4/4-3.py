# 왕실의 나이트
# sol
start = input()
row = int(start[1])
col = int(ord(start[0])) - int(ord('a')) + 1  # 입력된 문자 column을 정수로 바꾸기

# 나이트가 이동할 수 있는 방향 정의
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (-2, 1), (-1, 2), (1, 1), (2, 1)]

# 8가지 방향에 대해 각 위치로 이동이 가능한지 확인
count = 0
for step in steps:
    # 이동하고자 하는 위치 확인
    next_row = row + step[0]
    next_col = col + step[1]
    # 해당 위치로 이동 가능하면(=벗어나지 않으면) 카운트
    if next_row >= 1 and next_row <= 8 and next_col >= 1 and next_col <= 8:
        count += 1

print(count)
