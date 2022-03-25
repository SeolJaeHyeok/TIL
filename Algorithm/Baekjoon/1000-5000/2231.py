import sys
input = sys.stdin.readline

n = int(input())
answer = []

# 생성자 구하기
for i in range(1, n + 1):
    tmp = 0
    tmp += i # N을 더하고

    # N의 각 자릿수를 더하기
    for j in str(i):
        tmp += int(j)

    # 결과가 입력받은 값과 같다면 생성자 추가
    if tmp == n:
        answer.append(i)

if answer:
    print(min(answer))
else:
    print(0)