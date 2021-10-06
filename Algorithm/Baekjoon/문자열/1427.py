# 1427, 삽입 정렬 이용
n = list(input())

for i in range(1, len(n)):
    for j in range(i, 0, -1):
        if int(n[j]) > int(n[j - 1]):
            n[j], n[j-1] = n[j-1], n[j]

for i in n:
    print(i, end='')


# 라이브러리 이용
n = list(input())

n.sort(reverse=True)

for i in n:
    print(i, end='')

# 퀵 정렬
def quick_sort(array):
    if len(array) <= 1:
        return array

    pivot = array[0]  # 피벗
    tail = array[1:]  # 피벗을 제외한 리스트

    left_side = [x for x in tail if x < pivot]  # 피벗보다 작은 부분
    right_side = [x for x in tail if x > pivot]  # 피벗보다 큰 부분

    # 피벗을 기준으로 좌우 부분에 대해 각각 퀵 정렬 호출하고 전체 리스트 결과 반환
    return quick_sort(right_side) + [pivot] + quick_sort(left_side)


n = list(input())
result = quick_sort(n)

for i in result:
    print(i, end='')

