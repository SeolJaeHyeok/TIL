# Valid Parentheses
# 스택 자료구조 이용, 49ms
def isValid(s: str):
    stack = []
    table = {
        ")": "(",
        "]": "[",
        "}": "{"
    }
    for char in s:
        # 왼쪽 괄호일 경우 스택에 푸시
        if char not in table:
            stack.append(char)
        # 오른쪽 괄호일 경우 테이블 상의 오른쪽 괄호의 값(왼쪽 괄호)이 스택에 마지막으로 추가된 왼쪽 괄호와 일치하지 않으면 올바르지 않은 괄호
        elif not stack or table[char] != stack.pop():
            return False

    return len(stack) == 0

print(isValid("()[]{}"))
print(isValid("(({}[[]]))"))
print(isValid("(]"))
print(isValid("()[{}]"))

"""
유효한 괄호를 판단할 때는 같은 모양의 왼쪽 괄호가 열리고 같은 모양의 오른쪽 괄호가 나오기 전까지 다른 모양의 오른쪽 괄호가 나온다면 이는 올바르지 않은 괄호
따라서 왼쪽 괄호('(', '[', '{')괄호가 나온다면 스택에 푸시하고 오른쪽 괄호(')', ']', '}')가 나오면 스택에서 pop하여 괄호가 짝이 맞는지 확인  
 
- 매핑 테이블을 만들어서 테이블 상에 존재하지 않으면 스택이 푸시하고
- 테이블 상에 존재한다면 해당 문자를 키값으로해서 테이블의 값과 스택에서 팝한 값과 같지 않으면 False, 모두 알맞게 팝이 됐으면 True
"""

