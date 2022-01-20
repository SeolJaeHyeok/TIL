import sys
input = sys.stdin.readline

n, m = map(int, input().split())
array = [int(input()) for _ in range(n)]

answer = 0
start = 0
end = max(array) * m # 심사에 걸리는 최대 시간 * 검사 인원 수
while start <= end:
    mid = (start + end) // 2
    # mid 시간 동안 검사 가능한 인원수
    totalP = 0
    # 심사를 받을 수 있는 인원 수 구하기
    for time in array:
        totalP += mid // time
    # mid 시간동안 m명 이상 검사하지 못할 경우
    if totalP < m:
        # 시작 값 늘리기
        start = mid + 1
    else: # m명 이상 검사 가능할 경우
        # 끝값 줄여주고
        end = mid - 1
        # 여기서 답 체크
        answer = mid

print(answer)
