import sys
input = sys.stdin.readline

n = int(input())

num = 666
count = 0
while True:
    # 해당 숫자 안에서 종말 숫자를 발견했을 경우 카운팅
    if str(num).find('666') != -1:
        count += 1

    # n번째 종말 숫자 출력
    if count == n:
        print(num)
        sys.exit()

    # 숫자 1씩 증가하면서 완전 탐색
    num += 1
