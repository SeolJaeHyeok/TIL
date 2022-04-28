import sys
input = sys.stdin.readline

s1 = input().rstrip()
s2 = input().rstrip()

d = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]

for i in range(1, len(s1) + 1):
    for j in range(1, len(s2) + 1):
        # 새로 비교하는 두 문자가 같다면
        if s1[i - 1] == s2[j - 1]:
            # 이전까지의 최대 LCS의 길이에 1을 더해준다
            d[i][j] = d[i - 1][j - 1] + 1
        else:
            # 만약 다르다면 각각의 행과 열에서 이전까지의 최대 LCS의 길이를 비교하여 더 큰 값으로 설정
            d[i][j] = max(d[i - 1][j], d[i][j - 1])

print(d[-1][-1])