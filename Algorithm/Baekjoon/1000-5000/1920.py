import sys
input = sys.stdin.readline

def binary_search(t):
    # 시작값과 끝값 설정
    start, end = 0, len(array) - 1
    while start <= end:
        # target 인덱스 구하기
        mid = (start + end) // 2

        if array[mid] == t: # 구하려는 값이 존재할 경우 1 반환
            return 1
        elif array[mid] < t: # 구하려는 값보다 작다면 시작값 증가
            start = mid + 1
        else: # 구하려는 값보다 크다면 끝값 감소
            end = mid - 1

    return 0

n = int(input())
array = list(map(int, input().split()))
array.sort() # 이분 탐색을 위한 정렬

m = int(input())
target = list(map(int, input().split()))

for i in range(len(target)):
    print(binary_search(target[i]))