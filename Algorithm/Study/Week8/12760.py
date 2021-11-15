n, m = map(int, input().split())

array = []
score = [0] * n
for i in range(n):
    array.append(sorted(list(map(int, input().split())), reverse=True))

tmp = [[] for _ in range(m)]
for i in range(m):
    for j in range(n):
        tmp[i].append(array[j][i])

for i in range(len(tmp)):
    max_val = max(tmp[i])
    for j in range(len(tmp[0])):
        if max_val == tmp[i][j]:
            score[j] += 1

for i in range(len(score)):
    if score[i] == max(score):
        print(i + 1, end=' ')



