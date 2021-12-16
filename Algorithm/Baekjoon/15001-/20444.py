"""
참조: https://david0506.tistory.com/34
"""
# binary search

n, k = map(int, input().split())

left, right = 0, n//2 + 1 # 시작값과 끝값 설정
check = False
while left < right:
    mid = (left + right) // 2 # 중간값
    now = (mid + 1) * (n - mid + 1) # 현재 색종이의 수
    if now == k:
        check = True

    if now > k: # 현재 색종이의 수가 더 크면 끝값 줄이고
        right = mid
    else: # 더 작으면 시작값을 키운다.
        left = mid + 1

if check:
    print('YES')
else:
    print('NO')
