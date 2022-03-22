import sys
input = sys.stdin.readline

s = input().rstrip()
t = list(input().rstrip())

# 뒤에서부터 주어진 연산을 역산하여 계산
for i in range(len(t) - 1, len(s) - 1, -1):
    if t[i] == 'A':
        # 1번째 연산 : 문자열 뒤에 A를 추가
        # 1번째 연산의 역산: 문자열 뒤에서 A를 제거
        t.pop(i)
    elif t[i] == 'B':
        # 2번째 연산: 문자열을 뒤집고 뒤에 B를 추가
        # 2번째 연산의 역산: 문자열 뒤에서 B를 제거하고 문자열 뒤집기
        t.pop(i)
        t.reverse()

# 모든 연산 후의 남은 문자열이 s와 같으면 변환 가능 다르면 변환 불가능
if ''.join(t) == s:
    print(1)
else:
    print(0)