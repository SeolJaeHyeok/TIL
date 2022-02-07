import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    num = int(input())
    answer = defaultdict(int)
    i = 2 # 분모
    while True:
        # 1이 되면 종료
        if num == 1:
            break
        # 나눠질 수 있을 때까지 나누고 횟수 추가
        if num % i == 0:
            answer[i] += 1
            num /= i
            continue
        i += 1

    # 출력
    for k, v in answer.items():
        print(k, v)