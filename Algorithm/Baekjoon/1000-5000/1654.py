import sys
input = sys.stdin.readline

k, n = map(int, input().split())
array = []
for _ in range(k):
    array.append(int(input()))

# 시작 값, 끝 값 초기화
start, end = 1, max(array)
answer = 0
while start <= end:
    count = 0
    mid = (end + start) // 2

    # 만들 수 있는 랜선 개수 구하기
    for i in range(len(array)):
        count += array[i] // mid

    # n개보다 많이 만들었을 경우 정답 처리 후 시작값 증가
    if count >= n:
        answer = max(answer, mid)
        start = mid + 1
    else: # 적게 만들었을 경우 끝값 감소
        end = mid - 1

print(answer)