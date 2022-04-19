# 시간 초과
import sys
input = sys.stdin.readline

t = int(input())

def process(r1, c1, r2, c2, v):
    r1 -= 1
    c1 -= 1

    for i in range(r1, r2):
        for j in range(c1, c2):
            board[i][j] += v


for _ in range(t):
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    op = []
    for _ in range(m):
        r1, c1, r2, c2, v = map(int, input().split())
        op.append((r1, c1, r2, c2, v))

    for r1, c1, r2, c2, v in op:
        process(r1, c1, r2, c2, v)

    # 행의 합
    sum_row = []
    for i in board:
        sum_row.append(sum(i))

    # 열의 합
    sum_col = []
    for i in range(n):
        tmp = 0
        for j in range(n):
            tmp += board[j][i]
        sum_col.append(tmp)

    print(*sum_row)
    print(*sum_col)


import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]

    sum_row = [] # 각 행의 합을 저장할 리스트
    sum_col = [] # 각 열의 합을 저장할 리스트

    # 초기 배열의 행의 합과 열의 합 구하기
    for i in board:
        sum_row.append(sum(i))

    for i in range(n):
        tmp = 0
        for j in range(n):
            tmp += board[j][i]
        sum_col.append(tmp)

    # 연산의 횟수만큼 반복
    for _ in range(m):
        r1, c1, r2, c2, v = map(int, input().split())

        # (r1, c1) ~ (r2, c2) 범위 안에서 연산으로 변화하는 값의 총합 = 범위 안에 포함된 행과 열에 해당하는 좌표의 개수 * v
        """
        ex)
        연산의 조건이 1 1 2 3 3로 주어지고 배열이 아래와 같이 주어졌을 경우 
        1 2 3
        4 5 6
        7 8 9
        
        1. 행과 열의 변화
        (1, 1)부터 (2, 3)까지의 각 좌표값이 v만큼 변화하는 행은
        총 (2 - 1 + 1)개의 행에서 (3 - 1 + 1)개의 열이 변화한다고 할 수 있다.
        다시 말해, 범위에 해당하는 2개의 행과 각 행의 3개의 열에 각각 v만큼 더해진다고 말할 수 있다.
        
        2. 위 같은 정의를 바탕으로 아래와 같이 풀이할 수 있다.
        1) 행의 변화값
        초기에 각 행과 열의 합을 따로 관리하고 있기 때문에
        각 행의 합을 저장하는 배열의 해당하는 범위(r-1 ~ r2)에 (변화하는 열의 개수 * v)를 더해주면 해당 행의 총 변화값과 일치
        -> r - 1인 이유는 1번째 행의 합은 0번째 인덱스에 저장, 2번째 행의 합은 1번째 인덱스에 저장, 3번째 행의 합은 2번째 인덱스에 저장 ... 
           위와 같이 저장하고 있기 때문
        2) 열의 변화값
        위와 동일하게 각 열의 합을 저장하는 배열의 해당하는 범위(c-1 ~ c2)에 (변화하는 행의 개수 * v)를 더해주면 해당 열의 총 변화값과 일치
        -> 마찬가지로 c - 1인 이유는 1번째 열의 합은 0번째 인덱스에 저장, 2번째 열의 합은 1번째 인덱스에 저장, 3번째 열의 합은 2번째 인덱스에 저장 ... 
           위와 같이 저장하고 있기 때문 
        """
        for i in range(r1 - 1, r2):
            sum_row[i] += (c2 - c1 + 1) * v

        for i in range(c1 - 1, c2):
            sum_col[i] += (r2 - r1 + 1) * v

    print(*sum_row)
    print(*sum_col)