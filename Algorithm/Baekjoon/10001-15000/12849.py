import sys
input = sys.stdin.readline

# 0 = 정보과학관 1 = 전산관 2 = 미래관 3 = 신양 4 = 한경직 5 = 진리 6 = 형남 7 = 학생회관
"""
n분 후 정보과학관으로 돌아오는 방법의 수 = n - 1분까지 전산관에 도착할 수 있는 수 + n - 1분까지 미래관에 도착할 수 있는 수
"""
def process():
    global d
    tmp = [0 for _ in range(8)]
    # n분 후 각 건물에 올 수 있는 경우의 수를 해당 건물과 연결된 건물에 n-1분까지 올 수 있는 경우의 수를 더해준다.
    # 즉, tmp는 n분 후의 경우의 수를 뜻하고 d는 n-1분 후의 경우의 수를 뜻한다.
    tmp[0] = d[1] + d[2]
    tmp[1] = d[0] + d[2] + d[3]
    tmp[2] = d[0] + d[1] + d[3] + d[4]
    tmp[3] = d[1] + d[2] + d[4] + d[5]
    tmp[4] = d[2] + d[3] + d[5] + d[6]
    tmp[5] = d[3] + d[4] + d[7]
    tmp[6] = d[4] + d[7]
    tmp[7] = d[5] + d[6]

    # 조건에 따른 나머지 연산
    for i in range(8):
        tmp[i] %= 1000000007

    # 계산이 끝난 후 갱신된 값을 반환
    return tmp

n = int(input())
d = [1, 0, 0, 0, 0, 0, 0, 0]

for i in range(n):
    d = process()

print(d[0])
