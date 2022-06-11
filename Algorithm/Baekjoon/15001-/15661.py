import sys
input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
answer = 1e9


# 선택된 팀의 개수, 트리의 깊이, 선택된 팀을 제외하고 선택한 팀의 개수
def dfs(t, d, k):
    global answer

    # 트리의 깊이가 n과 같으면, 끝까지 모든 팀을 본 것이므로 종료
    if d == n:
        return

    if t == k:
        start = link = 0
        for i in range(n):
            for j in range(n):
                # 2번 3번 팀이 선택된 것이라면,board[2][3]+board[3][2]
                if team[i] and team[j]:
                    start += board[i][j]
                # 0번 1번이 남았으면, board[0][1]+board[1][0]
                elif not team[i] and not team[j]:
                    link += board[i][j]

        answer = min(answer, abs(start - link))
    else:
        team[d] = True
        dfs(t + 1, d + 1, k) # 팀을 선택한 경우
        team[d] = False
        dfs(t, d + 1, k) # 팀을 선택하지 않은 경우


for k in range(1, int(n // 2) + 2):
    team = [False] * (n + 1)
    dfs(0, 0, k)

print(answer)