# 주몽
# 투 포인터 이용
n = int(input())
m = int(input())
array = list(map(int, input().split()))
# 투 포인터를 위한 정렬
array.sort()

# 왼쪽 포인터와 오른쪽 포인터 초기화
count, left, right = 0, 0, len(array) - 1
while left < right:
    # 왼쪽 포인터의 값이 m 보다 크면 탈출
    if array[left] > m:
        break
    else:
        # 왼쪽 포인터의 값과 오른쪽 포인터의 값의 합이 m보다 큰 경우 오른쪽 포인터 조정
        if array[left] + array[right] > m:
            right -= 1
        # 오른쪽 포인터의 값과 왼쪽 포인터의 값의 합이 m보다 큰 경우 왼쪽 포인터 조정
        elif array[left] + array[right] < m:
            left += 1
        # 왼쪽 포인터의 값과 오른쪽 포인터의 값의 합이 m인 경우 양쪽 포인터 조정 후 카운팅
        else:
            left += 1
            right -= 1
            count += 1

print(count)




