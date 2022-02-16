import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    coins = list(map(int, input().split()))
    target = int(input())
    d = [0] * (target + 1)
    d[0] = 1

    for i in coins:
        for j in range(i, target + 1):
            d[j] += d[j - i]

    print(d)

"""
- target을 만들 수 있는 모든 경우의 수를 담을 dp테이블 선언
- 작은 단위의 동전부터 해당 동전으로 만들 수 있는 경우의 수 추가
- 동전의 단위가 늘어날수록 이전 동전의 단위에서 가능한 경우에 수에 추가 시켜준다.
d[n] = d[n] + d[n-동전의 단위]
ex) 동전의 단위가 1,2이고 4를 만들 수 있는 경우의 수
1) 동전의 단위가 1일 때 1 ~ 4까지 만들 수 있는 경우의 수는 모두 1
2) 동전의 단위가 2일 때 2 ~ 4까지 만들 수 있는 경우의 수는 
   ex) 4를 만드는 경우의 수는 (1, 1, 1, 1), (1, 1, 2), (2, 2) 총 3가지
       위 경우를 분해해보면
       newValue = (1, 1, 1, 1) + (1, 1, 2), (2, 2)
       즉, 갱신되는 값 = 이전 단위로 만들 수 있는 경우의 수 + 이전 단위로 만들 수 있는 경우의 수에서 동전의 단위를 뺀 경우의 수
"""