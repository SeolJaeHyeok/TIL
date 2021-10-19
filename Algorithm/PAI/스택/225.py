# Implement Stack using Queues
# 1, 47ms
from collections import deque

class MyStack:
    def __init__(self):
        self.stack = deque()

    def push(self, x: int):
        self.stack.append(x)

    def pop(self) -> int:
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def empty(self) -> bool:
        return len(self.stack) == 0


# 2, 45ms
class MyStack:
    def __init__(self):
        self.stack = deque()

    def push(self, x: int):
        self.stack.append(x)
        # 요소 삽입 후 맨 앞에 두는 상태로 재정렬
        for _ in range(len(self.stack) - 1):
            self.stack.append(self.stack.popleft())

    def pop(self) -> int:
        return self.stack.popleft()

    def top(self) -> int:
        return self.stack[0]

    def empty(self) -> bool:
        return len(self.stack) == 0

