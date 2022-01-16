import sys
input = sys.stdin.readline

n, m = map(int, input().split())

array = []
for i in range(n):
    array.append(int(input()))

answer = 0
start = 0
end = sum(array)
while start <= end:
    mid = (start + end) // 2    # 인출할 금액
    now = mid                   # 현재 가진 돈
    flag = False
    count = 1                   # 인출 횟수
    for i in array:
        # 설정한 금액이 사용할 금액보다 작을 경우
        if mid < i:
            flag = True
            break
        # 현재 가진 돈이 부족하면 인출
        if now < i:
            now = mid
            count += 1
        # 가진 돈으로 살 수 있는 만큼 살기
        now -= i

    # 설정 금액이 사용할 금액보다 작을 경우
    if flag:
        # 시작값 증가시키기
        start = mid + 1
    else:
        # 인출 횟수가 m보다 작거나 같은 경우
        if count <= m:
            # 끝값 줄이고 값 저장
            end = mid - 1
            answer = mid
        else:
            # 인출 횟수가 m보다 큰 경우 시작값 증가
            start = mid + 1

print(answer)
