# 돌려 돌려 돌림판
t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    x = ''.join(list(map(str, input().split())))
    y = ''.join(list(map(str, input().split())))
    board = input().split()
    count = 0

    for i in range(n):  # 돌림판 첫 번째 자리수부터
        z = ''  # m개 자리수 문자열
        for j in range(m):  # m개 만큼 추가하여 저장
            z += board[(i + j) % n]  # 나머지 연산 이용하여 인덱스 구하기
        if int(x) <= int(z) <= int(y):
            count += 1

    print(count)











# 1
# 6 3
# 0 0 0
# 9 9 9
# 1 2 3 4 5 6