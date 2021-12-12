# 2750
# 1, 정렬 라이브러리 이용 - 124ms
n = int(input())

array = []
for i in range(n):
    array.append(int(input()))

array.sort()
for i in array:
    print(i)

# 2, 선택 정렬 이용 - 200ms
n = int(input())

array = []
for i in range(n):
    array.append(int(input()))

for i in range(len(array)):
    min_index = i  # 가장 작은 원소의 인덱스
    for j in range(i + 1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[min_index], array[i] = array[i], array[min_index]

for i in array:
    print(i)


# 3, 삽입 정렬 이용 - 312ms
n = int(input())

array = []
for i in range(n):
    array.append(int(input()))

for i in range(1, len(array)):
    for j in range(i, 0, -1):
        # 자기보다 큰 데이터를 만나면 스왑
        if array[j] < array[j - 1]:
            array[j - 1], array[j] = array[j], array[j - 1]
        else:  # 자기보다 작은 데이터를 만나면 그자리에서 멈춤
            break

for i in array:
    print(i)

