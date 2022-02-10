import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    bit = int(input())
    d = [[0] * 10 for _ in range(bit)]

    answer = 0
    # n이 1일 경우 모든 원소의 값은 1
    for i in range(10):
        d[0][i] = 1
        answer += 1

    for i in range(1, bit):
        # 다음 행의 첫번째 원소의 값은 이전 행의 모든 원소의 합
        d[i][0] = sum(d[i - 1])
        for j in range(1, 10):
            # 점화식대로 테이블 채우고 개수 세기
            d[i][j] = d[i][j - 1] - d[i - 1][j - 1]
            answer += d[i][j]

    print(answer)