l, r = input().split()
word = input()

keyboard = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
table = {}

# 딕셔너리로 각 키보드의 좌표 저장
for i in range(len(keyboard)):
    for j in range(len(keyboard[i])):
        table[keyboard[i][j]] = (i, j)

# 왼손, 오른손 시작 좌표
lx, ly = table[l]
rx, ry = table[r]

answer = 0
# 모음 체크를 위한 문자열
check = 'yuiophjklbnm'
for char in word:
    # 이동한 좌표
    nx, ny = table[char][0], table[char][1]
    if char in check: # 모음이면 rx, ry로 계산
        answer += abs(rx - nx) + abs(ry - ny) + 1
        rx, ry = nx, ny
    else: # 자음이면 lx, ly로 계산
        answer += abs(lx - nx) + abs(ly - ny) + 1
        lx, ly = nx, ny

print(answer)

