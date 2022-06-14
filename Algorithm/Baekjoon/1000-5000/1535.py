import sys
input = sys.stdin.readline

n = int(input())
power = [0] + list(map(int, input().split()))
happy = [0] + list(map(int, input().split()))
d = [[0] * 101 for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, 101):
        if power[i] <= j:
            d[i][j] = max(d[i - 1][j], d[i - 1][j - power[i]] + happy[i])
        else:
            d[i][j] = d[i - 1][j]

print(d[n][99])


# 배낭문제 참조 블로그: https://gsmesie692.tistory.com/113?category=523232