# 거스름 돈
n = int(input())
count = 0

mList = [500, 100, 50, 10]  # 큰 단위의 화폐부터 차례대로 확인

for coin in mList:
    count += n // coin  # n을 coin으로 나눴을 때의 몫(해당 화폐로 나누어 줄 수 있는 최대 개수)을 카운트 해주고
    n %= coin  # 해당 화폐로 거슬러 주고 난 뒤 남은 돈

print(count)
