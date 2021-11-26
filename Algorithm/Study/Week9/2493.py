n = int(input())
towers = list(map(int, input().split()))
result = [0] * len(towers)
stack = []

for i, cur in enumerate(towers):
    while stack:
        if cur < towers[stack[-1]]:
            result[i] = stack[-1] + 1
            break
        else:
            stack.pop()

    stack.append(i)
    print(stack)

for i in result:
    print(i, end=' ')

"""
LeetCode 739번 Daily Temperatures 문제와 완전히 동일한 로직

- 완전 탐색으로 구현하면 시간초과가 발생하므로 스택 자료구조를 사용해서 구현해야 한다.
- 우선 스택에는 현재까지의 가장 높은 탑의 위치가 인덱스로 담긴다.
- if cur < towers[stack[-1]] <- 이 조건을 통해 이전까지의(왼쪽 방향으로 가장 가까운) 가장 높은 탑의 높이와 현재 탑의 높이를 비교하여
  현재 탑의 높이가 낮다면 이전까지의(왼쪽 방향으로 가장 가까운) 가장 높은 탑의 위치를 결과에 추가해준다. 
  여기서 위치는 인덱스로 저장되어 있으므로 +1을 해서 추가한다.
- 만약 현재 탑의 높이가 더 높다면 이전까지의 가장 높은 탑의 위치를 제거한다. 

"""
