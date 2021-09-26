# 만들 수 없는 금액
# false
n = int(input())
coin = list(map(int, input().split()))
coin.sort()

result = set()
start = coin[0]
for i in range(1, len(coin)):
    for j in range(len(coin) - i+1):
        result.add(coin[j+i])
    start = coin[i]
print(result)

# sol
n = int(input())
data = list(map(int, input().split()))
data.sort()

target = 1
for x in data:
    # 만들 수 없는 금액을 찾았을 때 반복 종료
    if target < x:
        break
    target += x

# 만들 수 없는 금액 출력
print(target)

"""
접근 방법
- 화폐 단위를 기준으로 오름차순 정렬
- 그런 다음 1부터 차례대로 특정한 금액(target)을 만들 수 있는지 확인(현재 확인하는 동전의 단위가 target 이하인지 확인)
- target을 만들 수 있다면 target 업데이트
"""