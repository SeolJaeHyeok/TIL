import sys
input = sys.stdin.readline

n = int(input())
array = []
for _ in range(n):
    array.append(list(map(int, input().split())))


def process(x, y):
    count = 0
    for i in range(x, x + 3):
        for j in range(y, y + 3):
            if array[i][j] == 1:
                count += 1
    return count

answer = 0
for i in range(n - 2):
    for j in range(n - 2):
        answer = max(answer, process(i, j))

print(answer)