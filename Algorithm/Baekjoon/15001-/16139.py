# 1, 50점
import sys
input = sys.stdin.readline

word = input().rstrip()
q = int(input())
for _ in range(q):
    target, l, r = map(str, input().split())
    l = int(l)
    r = int(r)
    print(word[l:r + 1].count(target))

# 2, 100점
import sys
input = sys.stdin.readline

word = input().rstrip()
q = int(input())

# 주어진 단어에 등장한 알파벳을 누적
# table[i][0 ~ 25] = i번째 단어일 때 그동안 누적된 a~z까지의 알파벳
table = [[0] * 26 for _ in range(len(word) + 1)]

for i in range(1, len(word) + 1):
    table[i][ord(word[i - 1]) - 97] = 1 # 등장한 단어 추가하고
    # 이전까지 등장한 값과 합쳐서 누적
    for j in range(26):
        table[i][j] += table[i - 1][j]

for _ in range(q):
    target, l, r = map(str, input().split())
    l, r = int(l), int(r)

    # [l, r] 구간에 target이 등장한 횟수 출력
    print(table[r + 1][ord(target) - 97] - table[l][ord(target) - 97])
