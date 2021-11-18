def solution(dirs):
    answer = set()
    # 이동 방향 정의
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    d_table = {"U": 0, "L": 1, "D": 2, "R": 3}

    # 시작은 0, 0
    x, y = 0, 0
    for d in dirs:
        # 이동할 좌표 nx, ny를 구하고
        idx = d_table[d]
        nx = x + dx[idx]
        ny = y + dy[idx]
        # 이동할 좌표가 범위를 벗어나면 무시
        if nx > 5 or nx < -5 or ny > 5 or ny < -5:
            continue
        # 범위 내에 있다면 추가, 길은 양방향으로 존재하므로 출발과 도착을 바꿔서 저장하는 예외처리도 필요
        answer.add((x, y, nx, ny))
        answer.add((nx, ny, x, y))
        # 좌표 이동
        x, y = nx, ny

    # 결과값 리턴 answer에 저장된 것은 출발과 도착이 바뀐 값까지 저장되어 있으므로 2로 나눠준다.
    return len(answer) // 2


print(solution("ULURRDLLU"))
print(solution("LULLLLLLU"))