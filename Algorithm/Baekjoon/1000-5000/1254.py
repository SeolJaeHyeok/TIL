import sys
input = sys.stdin.readline

s = input().rstrip()

# 문자열의 오른쪽으로 새로운 문자가 추가되어야 하므로 가장 왼쪽부터 팰린드롬 여부 판별
for i in range(len(s)):
    if s[i:] == s[i:][::-1]:
        print(len(s) + i)
        break
