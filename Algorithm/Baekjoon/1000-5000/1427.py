# 1427, 삽입 정렬 이용
# 데이터를 역순으로 정렬하는 것이기 때문에 일반적인 오름차순 정렬과는 값의 비교가 반대
n = list(input())

for i in range(1, len(n)):
    for j in range(i, 0, -1):
        if int(n[j]) > int(n[j - 1]):  # 자신의 왼쪽에 있는 데이터보다 크다면 스왑
            n[j], n[j-1] = n[j-1], n[j]
        else:  # 자기보다 작은 데이터를 만나면 반복문 탈출 why? 특정 데이터의 왼쪽에 있는 데이터들은 이미 정렬이 된 상태이기 때문에
            break

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

