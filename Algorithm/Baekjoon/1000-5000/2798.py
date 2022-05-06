import sys
input = sys.stdin.readline

n, m = map(int, input().split())
cards = list(map(int, input().split()))

answer = 0
# 완전 탐색
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            # 세장의 카드의 합이 m 이하일 경우 값 갱신
            if cards[i] + cards[j] + cards[k] <= m:
                answer = max(answer, cards[i] + cards[j] + cards[k])

print(answer)