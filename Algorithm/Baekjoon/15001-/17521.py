import sys
input = sys.stdin.readline

n, w = map(int, input().split())
flows = [int(input()) for _ in range(n)]

coin, cash = 0, 0
flag = True

for day, price in enumerate(flows):
    if day == 0:
        coin += w // price
        cash += w % price

    if day == n - 1:
        cash += price * coin
        break

    if flows[day] <= flows[day + 1]: # 상승 곡선
        if not flag: # 상승 곡선이었다가 다음 지점부터 하강 곡선으로 변경되는 변곡점에 매도
            coin += cash // price
            cash -= price * coin
        flag = True
    else: # 하강 곡선
        if flag: # 하강 곡선이었다가 다음 지점부터 상승 곡선으로 변경되는 변곡점에 매수
            cash += price * coin
            coin = 0
        flag = False

print(cash)