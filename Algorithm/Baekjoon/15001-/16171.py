import sys
input = sys.stdin.readline

s = input().rstrip()
k = input().rstrip()

# 숫자 제거
tmp = ''
for char in s:
    if char.isdecimal():
        continue

    tmp += char

# 숫자 제거한 문자열 안에 k가 존재하는지 체크
# 단, 연속하는 문자열이어야만 한다.
flag = False
for i in range(len(tmp) - len(k) + 1):
    word = tmp[i] # 탐색 시작 문자

    # 시작 문자부터 길이가 k와 같을때까지 연속된 문자를 더해주고
    for j in range(i + 1, i + len(k)):
        word += tmp[j]

    # 그 문자열이 k와 같을 경우 탈출
    if word == k:
        flag = True
        break

if flag:
    print(1)
else:
    print(0)
