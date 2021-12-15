import sys

N = int(input())
cmd = {}
for _ in range(N):
    p, i, q = sys.stdin.readline().split()
    try:
        cmd[p].append(q)
    except:
        cmd[p] = [q]

ans = []
visited = {}
q = ['Baba']  # Baba 부터 시작
# bfs 탐색
for now in q:
    try:
        for c in cmd[now]:
            if c not in visited:
                visited[c] = 1
                q.append(c)
                ans.append(c)
    except:
        continue

for a in sorted(ans):
    print(a)
