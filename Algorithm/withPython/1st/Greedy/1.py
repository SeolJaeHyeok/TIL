# 모험가 길드
# false
n = int(input())
rate = list(map(int, input().split()))

count = 0
while True:
    max_rate = max(rate)
    if (len(rate) // max_rate) > 0:
        count += 1
        
        rate.remove(max_rate)
        for i in range(max_rate - 1):
            rate.remove(rate[i])
    else:
        break

# sol
n = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0  # 총 그룹의 수
count = 0  # 현재 그룹에 포함된 모험가의 수

for i in data:  # 공포도가 낮은 것부터 하나씩 확인하여
    count += 1  # 현재 그룹에 해당 모험가 포함시키기
    if count >= i:  # 현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면, 그룹 결성
        result += 1  # 총 그룹의 수 증가
        count = 0  # 현재 그룹에 포함된 모험가의 수 초기화

print(result)


"""
접근 방법
- 공포도를 기준으로 오름차순으로 정렬한 뒤
- 공포도가 가장 낮은 모험가부터 하나씩 확인하여 그룹에 포함될 모험가의 수를 계산
- 현재 그룹에 포함된 모험가의 수가 확인하고 있는 공포도보다 크다면 그룹을 결성 
- 공포도가 오름차순으로 정렬되어 있다는 점에서 항상 최소한의 모험가의 수만 포함하여 그룹을 결성하게 된다.
"""