import sys
input = sys.stdin.readline

# 1, 이진 탐색
n = int(input())
array = list(map(int, input().split()))
array.sort()
m = int(input())
orders = list(map(int, input().split()))

# 손님의 요청한 부품을 하나씩 확인
for target in orders:
    flag = False # 존재하는지를 체크할 변수
    start = 0 # 시작값
    end = len(array) - 1 # 끝값
    while start <= end:
        mid = (start + end) // 2 # 중간값
        if array[mid] == target: # 찾았을 경우
            flag = True
            break
        elif array[mid] < target: # 손님이 요청한 부품이 중간값보다 클 경우
            start = mid + 1 # 시작값 갱신
        elif array[mid] > target: # 손님이 요청한 부품이 중간값보다 작을 경우
            end = mid - 1 # 끝값 갱신

    # 존재 여부에 따라 출력
    if flag:
        print('yes', end=" ")
    else:
        print('no', end=" ")


# 2, 계수 정렬
n = int(input())
array = list(map(int, input().split()))

tmp = [0] * 1000001
for i in array:
    tmp[i] = 1

m = int(input())
orders = list(map(int, input().split()))

for i in orders:
    if tmp[i]:
        print('yes', end=' ')
    else:
        print('no', end=' ')

# 3, set 자료형
n = int(input())
array = set(map(int, input().split()))
m = int(input())
orders = list(map(int, input().split()))

for i in orders:
    if i in array:
        print('yes', end=' ')
    else:
        print('no', end=' ')

# 5
# 8 3 7 9 2
# 3
# 5 7 9