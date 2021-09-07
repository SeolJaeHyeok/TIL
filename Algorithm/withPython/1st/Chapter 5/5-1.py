stack = []

# 삽입
stack.append(5)
stack.append(2)
stack.append(4)
stack.append(7)
stack.pop()
stack.append(3)
stack.append(9)
stack.pop()

print(stack) # 최하단 원소부터 출력
print(stack[::-1]) # 최상단 원소부터 출력