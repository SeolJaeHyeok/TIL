"""
행복한 수열의 개수
1~100 사이의 숫자로만 이루어져 있는 n * n 크기의 격자 정보가 주어집니다.

이때 행복한 수열이라는 것은 다음과 같이 정의됩니다.

행복한 수열 = 연속하여 m개 이상의 동일한 원소가 나오는 순간이 존재하는 수열
n * n 크기의 격자 정보가 주어졌을 때 각 행마다 봤을 때 나오는 n개의 수열과,
각 열마다 봤을 때 나올 수 있는 n개의 수열을 포함하여 총 2n개의 수열 중 행복한 수열의 개수를 세서 출력하는 프로그램을 작성해보세요.

입력 형식
첫 번째 줄에는 격자의 크기를 나타내는 n과 연속해야 하는 숫자의 수를 나타내는 m이 공백을 사이에 두고 주어집니다.

두 번째 줄부터는 n개의 줄에 걸쳐 격자에 대한 정보가 주어집니다. 각 줄에는 각각의 행에 대한 정보가 주어지며,
이 정보는 1에서 100사이의 숫자로 각각 공백을 사이에 두고 주어집니다.

1 ≤ m ≤ n ≤ 100
출력 형식
2n개의 수열들 중 행복한 수열의 수를 출력해주세요.
"""

# My, 46%
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
array = []
for _ in range(n):
    array.append(list(map(int, input().split())))

answer = 0
for i in range(n):
    count = 1
    for j in range(1, n):
        if array[i][j] == array[i][j - 1]:
            count += 1

    if count >= m:
        answer += 1

for i in range(n):
    count = 1
    for j in range(1, n):
        # print(array[j][i], array[j - 1][i])
        if array[j][i] == array[j - 1][i]:
            count += 1

    if count >= m:
        answer += 1

print(answer)


# Sol
# 변수 선언 및 입력:
n, m = tuple(map(int, input().split()))
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
seq = [0 for _ in range(n)]


def is_happy_sequence():
    # 주어진 seq가 행복한 수열인지 판단하는 함수입니다.
    consecutive_count, max_ccnt = 1, 1
    for i in range(1, n):
        if seq[i - 1] == seq[i]:
            consecutive_count += 1
        else:
            consecutive_count = 1

        max_ccnt = max(max_ccnt, consecutive_count)

    # 최대로 연속한 회수가 m이상이면 true를 반환합니다.
    return max_ccnt >= m


num_happy = 0

# 먼저 가로로 행복한 수열의 수를 셉니다.
for i in range(n):
    seq = grid[i][:]

    if is_happy_sequence():
        num_happy += 1

# 세로로 행복한 수열의 수를 셉니다.
for j in range(n):
    # 세로로 숫자들을 모아 새로운 수열을 만듭니다.
    for i in range(n):
        seq[i] = grid[i][j]

    if is_happy_sequence():
        num_happy += 1

print(num_happy)