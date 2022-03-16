import sys
input = sys.stdin.readline

g = int(input())
past = [i for i in range(1, 100001)] # 범위 내의 기억하고 있는 모든 몸 무게 리스트
now = [i for i in range(1, 100001)] # 범위 내의 현재의 모든 몸 무게 리스트

answer = []
left, right = 0, 0
while left < 100000 and right < 100000:
    # 현재 몸무게의 제곱 - 기억하고 있던 몸무게의 제곰 = (A^2 - B^2) = (A + B) * (A - B)
    tmp_weight = (now[left] + past[right]) * (now[left] - past[right])

    if tmp_weight == g:
        answer.append(now[left])

    if tmp_weight < g: # g보다 작으면 현재 몸무게 증가
        left += 1
    else: # 크면 기억하고 있던 몸무게 증가
        right += 1

if answer:
    for i in answer:
        print(i)
else:
    print(-1)

