import sys
input = sys.stdin.readline

n = int(input())
x, y = 0, 0 # 시작 좌표
answer = time = 0 # 정답, 순회에 걸린 시간

# dir 방향으로 n만큼 이동시키는 함수
def process(dir, n):
    global x, y, answer, time

    for i in range(n):
        # 좌표 이동
        x = x + dx[dir]
        y = y + dy[dir]

        # 이동 시간 증가
        time += 1

        # 시작 좌표로 돌아왔다면
        if x == 0 and y == 0:
            # 시간 저장하고 True 반환
            answer = time
            return True

    # 원점으로 돌아가지 못하면 False 반환
    return False

# 동, 서, 남 북
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
dir = -1
for _ in range(n):
    l, n = map(str, input().split())
    n = int(n)

    # 이동 방향 설정
    if l == 'E':
        dir = 0
    elif l == 'W':
        dir = 1
    elif l == 'S':
        dir = 2
    else:
        dir = 3

    # 이동 방향에 따라 좌표 이동 시키기
    result = process(dir, n)

    # 원점으로 돌아온다면 출력 후 종료
    if result:
        print(answer)
        sys.exit()

print(-1)