import sys
input = sys.stdin.readline

a, b, c, m = map(int, input().split())

answer = 0 # 일 총합
total = 0 # 피로도의 총합
for i in range(24):
    if total + a <= m: # 현재 시간에서 일을 할 수 있는 경우
        # 일을 하고 피로도를 늘림
        answer += b
        total += a
    else: # 일을 할 수 없는 경우
        # 휴식을 취해 피로도를 줄여준다.

        # 피로도의 최소값을 0으로 설정
        if total - c >= 0:
            total -= c
        else:
            total = 0

print(answer)