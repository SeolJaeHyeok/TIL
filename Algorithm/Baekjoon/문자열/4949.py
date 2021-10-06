# 4949
import sys

def check(p):
    stack = []
    for i in p:
        # 왼쪽 괄호가 나올 경우
        if i == '(' or i == '[':
            stack.append(i)  # 스택에 push
        # 오른쪽 소괄호가 나올 경우
        elif i == ')':
            # 스택의 마지막에 추가된 괄호랑 짝이 맞으면 pop
            if stack and stack[-1] == '(':
                stack.pop()
            # 짝이 맞지 않으면 false
            else:
                return False
        # 오른쪽 대괄호가 나올 경우
        elif i == ']':
            # 스택의 마지막에 추가된 괄호랑 짝이 맞으면 pop
            if stack and stack[-1] == '[':
                stack.pop()
            # 짝이 맞지 않으면 false
            else:
                return False
    # 스택의 모든 원소가 빠져나가고(왼쪽 괄호와 오른쪽 괄호의 수가 같은 경우) true 리턴
    if not stack:
        return True

while True:
    s = sys.stdin.readline().rstrip()
    # 종료 조건
    if s == '.':
        break
    if check(s):
        print('yes')
    else:
        print('no')


"""
- 균형잡힌 괄호와 같은 문제는 스택 자료구조를 이용하면 쉽게 풀 수 있다.
- 스택은 FILO 정책이기 때문에 가장 마지막에 들어온 원소가 가장 빨리 빠져나간다.
- 때문에 괄호의 종류를 구분지어 모든 왼쪽 괄호를 스택에 추가시킨 후 짝이 맞는 오른쪽 괄호가 나온다면 스택에서 pop을 해준다.
- 예를 들어, '(([)])'와 같은 괄호가 입력이 됐다고 하면 
1. 모든 왼쪽 괄호가 스택에 들어가면 ['(', '(', '[']와 같이 추가가 될 것이다.
2. 다음 원소가 오른쪽 괄호인 ')'이므로 스택의 마지막에는 '('가 존재해야 괄호의 짝이 맞게 되고 균형잡힌 괄호가 성립할 것이다. 
3. 하지만 현재 스택의 마지막 원소는 왼쪽 대괄호 '['가 존재하기 때문에 괄호의 짝이 맞지 않고 균형잡힌 괄호가 성립하지 않는다.
4. 또한 문자열의 순회가 끝난 다음에는 스택이 비어있어야 한다. 
why? 스택에는 왼쪽 괄호가 추가가 될 것이고 그에 해당하는 오른쪽 괄호를 만나면 빠져 나가기 때문에
양 쪽 괄호의 숫자가 일치한다면 스택은 비어져 있을 것이기 때문이다. 
"""