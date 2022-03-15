import sys
input = sys.stdin.readline

# 두 원점 사이의 거리를 구하는 함수
def get_distance(a, b):
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2

def dfs(now):
    for i in range(n):
        # 원 A,B 가 교차한다면 A,B의 중심좌표 간의 거리가 (A의 반지름 + B의 반지름) 보다 작거나 같아한다.
        # 따라서 두 지점 사이의 거리가 통신 범위를 벗어나는 경우는 무시
        if get_distance(loc[now], loc[i]) > (loc[now][2] + loc[i][2]) ** 2 or visited[i] or now == i:
            continue
        visited[i] = True
        dfs(i)

t = int(input())
for _ in range(t):
    n = int(input())
    loc = []
    answer = 0
    visited = [False] * n
    for i in range(n):
        x, y, r = map(int, input().split())
        loc.append((x, y, r))

    for i in range(n):
        if not visited[i]:
            dfs(i)
            answer += 1

    print(answer)
