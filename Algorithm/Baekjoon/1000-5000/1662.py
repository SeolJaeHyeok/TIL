import sys
input = sys.stdin.readline

def process(word):
    stack = []
    length = 0 # 단어의 길이
    count = '' # 곱해줘야할 횟수
    for s in word:
        if s.isdigit():
            length += 1
            count = s
        elif s == '(':
            stack.append((length - 1, count))
            length = 0 # 단어 길이 초기화
        else: # 오른쪽 괄호일 경우
            # 단어 길이 계산
            if stack:
                l, cnt = stack.pop()
                length = (int(cnt) * length) + l

    return length

print(process(input()))

"""
33(562(71(9)))의 경우

stack = ('('를 만나기이전까지의 단어의 길이, 곱해줘야할 횟수)
1. stack = [(1, 3)]
2. stack = [(1, 3), (2, 2)]
3. stack = [(1, 3), (2, 2), (1, 1)]
위와 같이 스택에 추가

- ')'를 만나기 전까지 만난 숫자의 길이만큼 정답을 증가(여기서는 9, 즉 1만큼 증가)
- ')'를 만나면 스택에서 값을 꺼냄
- 새로운 숫자의 길이 = 이전까지의 숫자의 길이 * 곱해줘야할 횟수 + '('이후부터 등장한 숫자의 길이

33(562(71(9))) -> 33(562(79)) -> 33(567979) -> 3567979567979567979
"""