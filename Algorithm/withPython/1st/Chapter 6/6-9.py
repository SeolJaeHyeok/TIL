# 두 배열의 원소 교체
# my, 계수 정렬
n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

count = [0] * (max(b) + 1)  # 입력된 데이터 + 1의 크기만큼의 리스트 생성
sorted_a = sorted(a)  # 오름차순 정렬
sorted_b = []  # 계수 정렬된 리스트를 위한 빈 리스트 선언

for i in range(len(b)):
    count[b[i]] += 1  # 각 데이터의 값과 동일한 인덱스의 데이터를 1씩 증가

for i in range(len(count)):  # 리스트에 기록된 정렬 정보 확인
    for j in range(count[i]):
        sorted_b.append(i)  # 등장한 횟수만큼 리스트에 추가

for i in range(k):
    if sorted_a[i] < sorted_b[len(sorted_b) - 1 - i]:
        # Swap, a는 앞에서부터 k개 b는 뒤에서부터 k개
        sorted_a[i], sorted_b[len(sorted_b) - 1 - i] = sorted_b[len(sorted_b) - 1 - i], sorted_a[i]

print(sum(sorted_a))  # 합계 출력

# 계수 정렬 + 파이썬 정렬 라이브러리
n, k = map(int, input().split())
a = sorted(list(map(int, input().split())))  # 입력 받고 오름차순 정렬
b = list(map(int, input().split()))

count = [0] * (max(b) + 1)  # 입력된 데이터 + 1의 크기만큼의 리스트 생성
sorted_b = []  # 계수 정렬된 리스트를 위한 빈 리스트 선언

for i in range(len(b)):
    count[b[i]] += 1  # 각 데이터의 값과 동일한 인덱스의 데이터를 1씩 증가

for i in range(len(count)):  # 리스트에 기록된 정렬 정보 확인
    for j in range(count[i]):
        sorted_b.append(i)  # 등장한 횟수만큼 리스트에 추가

sorted_b.sort(reverse=True)  # 오름차순으로 추가된 데이터들을 내림차순으로 변경

for i in range(k):
    if a[i] < sorted_b[i]:
        # Swap, a는 앞에서부터 k개 b는 뒤에서부터 k개
        a[i], sorted_b[i] = sorted_b[i], a[i]

print(sum(a))  # 합계 출력

# my2, 파이썬 정렬 라이브러리 이용 풀이
n, k = map(int, input().split())
a = sorted(list(map(int, input().split())))  # a 리스트 입력받아 오름차순 정렬
b = sorted(list(map(int, input().split())), reverse=True)  # b 리스트 입력받아 내림차순 정렬

for i in range(k):  # k번 반복
    if a[i] < b[i]:  # a보다 b 값이 더 크면
        a[i], b[i] = b[i], a[i]  # Swap
    else:
        break

print(sum(a))  # 합계 출력
