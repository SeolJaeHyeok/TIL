import sys
from collections import defaultdict

input = sys.stdin.readline

while True:
    n, m = map(int, input().split())
    table = defaultdict(int)

    if n == 0 and m == 0:
        break

    info = [list(map(int, input().split())) for _ in range(n)]

    # 점수 카운팅
    for i in range(n):
        for j in range(m):
            table[info[i][j]] += 1

    # 점수 높은 유저 순으로 내림차순 정렬
    ranking = sorted(table.items(), key=lambda x: x[1], reverse=True)

    # 1등은 유일하므로 2등 선수를 정답에 추가하고 그 선수의 점수를 가지고 동점자 확인
    answer = [ranking[1][0]] # 2등 선수 추가
    second_score = ranking[1][1] # 2등 선수 점수

    # 동점자 확인
    for i in range(2, len(ranking)):
        user, score = ranking[i]
        if second_score == score:
            answer.append(user)
        else:
            break

    print(*sorted(answer))