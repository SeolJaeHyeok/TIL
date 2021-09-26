# 볼링공 고르기
# solve
n, m = map(int, input().split())
weight = list(map(int, input().split()))

count = 0
for i in range(len(weight)):
    start = weight[i]  # 시작점 정의
    for j in range(i+1, len(weight)):  # 위 시작점 다음 인덱스부터 리스트를 끝까지 순회
        if start != weight[j]:  # 시작점의 값과 같지 않으면 카운팅
            count += 1

print(count)

# sol
n, m = map(int, input().split())
data = list(map(int, input().split()))

# 1부터 10까지의 무게를 담을 수 있는 리스트
array = [0] * 11

for x in data:
    # 각 무게에 해당하는 볼링공의 개수 카운트
    array[x] += 1

result = 0
# 1부터 m까지의 각 무게에 대하여 처리
for i in range(1, m + 1):
    n -= array[i] # 무게가 i인 볼링공의 개수(A가 선택할 수 있는 개수) 제외
    result += array[i] * n # B가 선택하는 경우의 수와 곱해주기

print(result)


"""
접근 방법
- 입력된 무게 리스트에서 순서대로 시작점 업데이트 
- 정의된 시작점부터 끝까지 순회하며 같은 값이 아니면 카운팅
"""