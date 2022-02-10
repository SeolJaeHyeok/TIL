import sys
input = sys.stdin.readline

a, b = input(), input()

# 모든 문자를 순회할 수 있는 테이블 초기화
d = [[0] * (len(b)) for _ in range(len(a))]
answer = 0
# 한 문장의 모든 문자를 기준으로 다른 문장의 모든 문자를 순회
for i in range(len(a) - 1):
    for j in range(len(b) - 1):
        # 두 문자가 같은 경우 -> 이전까지의 값(연속된 문자의 개수) + 1
        if a[i] == b[j]:
            d[i][j] = d[i - 1][j - 1] + 1
            answer = max(answer, d[i][j])

print(answer)