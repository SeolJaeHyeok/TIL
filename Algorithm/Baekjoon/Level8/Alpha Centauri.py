# 1011번
"""
문제
https://www.acmicpc.net/problem/1011

풀이방법
1) 이동 회수(count)를 보면 1이 1번, 2가 1번, 3이 2번, 4가 2번, 5가 3번, 6이 3번 이런 식으로 나타나는 것을 볼 수 있다.
즉 이동 회수를 나타내는 숫자의 빈도수가 1,1,2,2,3,3,4,4, 이런 식으로 두 번씩 나타나는 규칙을 찾을 수 있다.
2) 이 빈도수에 해당하는 수를 더한 합은 count 숫자에 따라 이동 가능한 최대 거리를 나타낸다.
예를 들어 count가 6을 나타낸다면 count 6까지 우측 move distance 숫자를 합하면 12가 된다. (1+1+2+2+3+3 = 12)
"""


# 1
def solution(t):
    for _ in range(t):
        x, y = map(int, input().split())
        distance = y - x
        count = 0
        move = 1
        move_sum = 0
        while move_sum < distance:
            count += 1
            move_sum += move
            if count % 2 == 0:
                move += 1
        print(count)


T = int(input())
solution(T)

# 2
import math

T = int(input())

for _ in range(T):
    x, y = map(int, input().split())
    distance = y - x
    count = 0

    num = math.floor(math.sqrt(distance))   # n제곱 <= 거리 < (n+1)제곱일때 n제곱
    num_square = num ** 2   # n제곱의 제곱
    increase_num = math.sqrt(num_square)

    if distance > num_square + increase_num:
        count = 2 * num + 1
    elif num_square < distance <= num_square + increase_num:
        count = 2 * num
    elif distance == num_square:
        count = 2 * num - 1

    if distance < 4:
        count = distance

    print(count)