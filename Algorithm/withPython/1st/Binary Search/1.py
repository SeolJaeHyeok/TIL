# 정렬된 배열에서 특정 수의 개수 구하기
# 1, bisect 라이브러리 사용
from bisect import bisect_left, bisect_right

n, x = map(int, input().split())
array = list(map(int, input().split()))

left_side = bisect_left(array, x)
right_side = bisect_right(array, x)

if (right_side - left_side) > 0:
    print(right_side - left_side)
else:
    print(-1)


# 2, 함수 만들어 사용
# 값이 [left_value, right_value]인 데이터의 개수를 반환하는 함수
def count_by_range(array, left_value, right_value):
    right_index = bisect_right(array, right_value)
    left_index = bisect_left(array, left_value)
    return right_index - left_index

n, x = map(int, input().split()) # 데이터의 개수 N, 찾고자 하는 값 x 입력 받기
array = list(map(int, input().split())) # 전체 데이터 입력 받기

# 값이 [x, x] 범위에 있는 데이터의 개수 계산
count = count_by_range(array, x, x)

# 값이 x인 원소가 존재하지 않는다면
if count == 0:
    print(-1)
# 값이 x인 원소가 존재한다면
else:
    print(count)


"""
접근 방법
- 정렬이 된 배열이 입력되므로 값이 x인 원소의 개수는 x가 처음 등장하는 인덱스와 마지막에 등장하는 인덱스를 구해 그 차이를 구하면 된다.
"""
