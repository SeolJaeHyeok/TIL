s = input()

stack = []
count = 0
for char in s:
    if char == '(':  # 왼쪽 괄호라면 스택에 추가
        stack.append(char)
    elif stack and char == ')':  # 스택이 존재(왼쪽 괄호가 있는 상태)하고 오른쪽 괄호가 나오면 스택에서 제거
        stack.pop()
    else:  # 스택이 비어있는데 오른쪽 괄호가 나온다면 카운팅
        count += 1

# 만약 스택 안에 왼쪽 괄호가 존재한다면
# 그에 맞는 오른쪽 괄호가 추가되어야하므로 스택의 길이만큼 더해준다.
print(count + len(stack))
