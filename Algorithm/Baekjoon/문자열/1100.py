# 1100
# 1
array = []
for i in range(8):
    array.append(input())

count = 0
for i in range(len(array)):
    for j in range(len(array[i])):
        # 첫 번째가 하얀색일 경우
        if i % 2 != 0:
            if j % 2 != 0:
                if array[i][j] == 'F':
                    count += 1
        # 첫 번째가 검정색일 경우
        else:
            if j % 2 == 0:
                if array[i][j] == 'F':
                    count += 1

print(count)

# 2
array = []
for i in range(8):
    array.append(input())

count = 0
for i in range(len(array)):
    for j in range(len(array[i])):
        # 첫 번째가 하얀색일 경우
        if i % 2 != 0 and j % 2 != 0 and array[i][j] == 'F':
            count += 1
        # 첫 번째가 검정색일 경우
        elif i % 2 == 0 and j % 2 == 0 and array[i][j] == 'F':
            count += 1

print(count)

"""
- 조건에 따라 구현하면 풀 수 있는 문제
- 맨 왼쪽 위 다시 말해 첫 번째 줄은 하얀색으로 시작하고 검정색과 하얀색이 번갈아 가며 색칠되어 있다고 했으니 
두 번째 줄은 검정색으로 시작한다.
- 또한 하얀색으로 시작하는 줄은 홀수 칸이 하얀색이 될 것이고 검정색으로 시작하는 줄은 짝수 칸이 하얀색이 될 것이다. 
"""