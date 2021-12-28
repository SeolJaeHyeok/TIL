# 1, Fail
import sys

n, k, q, m = map(int, sys.stdin.readline().split())
sleep_arr = list(map(int, sys.stdin.readline().split()))
check_arr = list(map(int, sys.stdin.readline().split()))
s, e = map(int, sys.stdin.readline().split())

answer = set()
for i in check_arr:
    if i in sleep_arr:
        continue
    a = i
    while i <= e:
        answer.add(i)
        i += a

for i in sleep_arr:
    if i in answer:
        answer.remove(i)

print(n - len(answer))

# 2
n, k, q, m = map(int, sys.stdin.readline().split())
sleep_arr = list(map(int, sys.stdin.readline().split()))
check_arr = list(map(int, sys.stdin.readline().split()))

# 조는 학생 및 출석 코드를 받은 학생을 체크할 배열 선언
sleep_table = [0] * (n+3)
check_table = [0] * (n+3)

# 조는 학생 배열 추가
for i in sleep_arr:
    sleep_table[i] = 1

# 출석 코드를 받은 학생으로부터 출석 체크한 학생 추가
for i in check_arr:
    # 졸고 있는 학생이라면 무시
    if sleep_table[i]:
        continue
    # 그렇지 않으면 출석 코드를 받았고 졸고 있지 않은 학생들만 체크
    for j in range(i, n+3, i):
        if not sleep_table[j]:
            check_table[j] = 1

answer = [check_table[0]]
# i번째 학생까지 출석체크한 누적합 구하기
for i in range(1, n+3):
    answer.append(answer[-1] + check_table[i])


for _ in range(m):
    s, e = map(int, sys.stdin.readline().split())
    print(e-s+1 - (answer[e]-answer[s-1]))
