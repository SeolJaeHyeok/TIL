# 큰 수의 법칙
# my
n, m, k = map(int, input().split())
data = list(map(int, input().split()))
result = 0
k_count = 0

data.sort(reverse=True)

for i in range(m):  # m번 반복
    if k_count < k:  # 만약 k번 이하로 더했으면
        result += data[0]  # 가장 큰 수를 더하고
        k_count += 1  # 가장 큰 수를 몇 번 더했는지 확인하기 위해 k_count 1 더하기
    else:  # k번 이상 더했으면
        result += data[1]  # 두 번째로 큰 수 더하고
        k_count = 0  # k_count 초기화

print(result)

# sol1
# N, M, K 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())
# N개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

data.sort()  # 입력받은 수 정렬
first = data[0]  # 가장 큰 수
second = data[1]  # 두 번째로 큰 수

result = 0

while True:
    for i in range(k):  # 가장 큰 수 K번 더하기
        if m == 0:
            break
        result += first
        m -= 1  # 더할 때마다 1씩 빼기
    if m == 0:
        break
    result += second  # 두 번째로 큰 수 한 번 더하기
    m -= 1

print(result)

# sol2
# N, M, K 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())
# N개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

data.sort()  # 입력받은 수 정렬
first = data[0]  # 가장 큰 수
second = data[1]  # 두 번째로 큰 수

# 가장 큰 수가 더해지는 횟수 계산
count = int(m/(k + 1)) * k
count += m % (k + 1)

result = 0
result += count * first  # 가장 큰 수 더하기
result += (m - count) * second  # 두 번째로 큰 수 더하기

print(result)