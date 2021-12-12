# 1744
import sys

n = int(sys.stdin.readline())

array = []
for i in range(n):
    array.append(int(sys.stdin.readline()))

minus_array = []
plus_array = []
total = 0
for i in array:
    if i > 1:
        plus_array.append(i)
    elif i == 1:
        total += 1
    else:
        minus_array.append(i)

plus_array.sort(reverse=True)
minus_array.sort()

if len(minus_array) % 2 == 0:
    for i in range(0, len(minus_array), 2):
        total += minus_array[i] * minus_array[i + 1]
else:
    total += minus_array[-1]
    for i in range(0, len(minus_array) - 1, 2):
        total += minus_array[i] * minus_array[i + 1]

if len(plus_array) % 2 == 0:
    for i in range(0, len(plus_array), 2):
        total += plus_array[i] * plus_array[i + 1]
else:
    total += plus_array[-1]
    for i in range(0, len(plus_array) - 1, 2):
        total += plus_array[i] * plus_array[i + 1]

print(total)

"""
- 규칙을 찾는 것이 중요한 문제다. 
- 여기서 주의해야할 점이 바로 1이 입력됐을 때다. 1은 양수와 만나던 음수와 만나던 모두 더해주어야 최적의 해가 보장된다.
- 따라서 1이 입력되면 결과값에 바로 더해주고 1을 제외한 양수리스트와 음수 리스트로 나누어서 저장을 해준다.
- 그런 다음 양수 리스트를 내림차순으로 정렬하고 음수 리스트를 오름 차순으로 정렬해 준다.
- 이제 두 리스트를 각각 순회하면서 값을 찾아주면 되는데 
1. 리스트의 길이가 짝수인 경우 리스트의 원소들을 두 개씩 묶어서 곱해주면 최적의 해가 나온다.
2. 리스트의 길이가 홀수인 경우 리스트의 마지막 요소는 더해주고 나머지 요소들은 곱해주면 최적의 해가 나온다.  
"""

