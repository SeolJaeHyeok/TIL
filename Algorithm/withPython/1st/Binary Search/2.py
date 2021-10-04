# 고정점 찾기
def binary_search(array, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    # 고정점을 찾은 경우 인덱스 반환
    if array[mid] == mid:
        return mid
    elif array[mid] > mid:
        return binary_search(array, start, mid - 1)
    elif array[mid] < mid:
        return binary_search(array, mid + 1, end)


n = int(input())
array = list(map(int, input().split()))

index = binary_search(array, 0, n - 1)

if index == None:
    print(-1)
else:
    print(index)


"""
이진 탐색을 수행할 때는 찾고자 하는 값(target)이 중간값과 같다고 가정하고 탐색을 시작한다.
target이 중간값(array[mid])보다 작으면 끝값을 중간값-1로 갱신하여 다시 탐색하고 
target이 중간값(array[mid])보다 크다면 시작값을 중간값+1로 갱신하여 다시 탐색한다.
그렇게 범위를 1/2씩 줄여나가면서 탐색을 하다가 중간값과 찾고자 하는 값이 같으면 해당 결과를 리턴해주면 된다.
이 문제에서는 찾고자하는 값이 mid의 값과 같기 때문에 조건을 설정한 후 mid를 반환해주면 된다.
"""
