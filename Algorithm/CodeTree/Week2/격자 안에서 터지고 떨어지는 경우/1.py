"""
n개의 층으로 이루어진 1차원 젠가의 상태가 주어집니다.
각 층마다 1개의 블럭이 놓여져 있고, 각 블럭에는 1에서 100 사이의 숫자가 하나씩 적혀있습니다.

이 때 2번에 걸쳐 특정 구간의 블럭들을 빼는 작업을 진행하려 합니다.

처음에 위에서부터 2번째 블럭에서 4번째 블럭까지 블럭을 빼게 된다면, 남은 블럭은 중력에 의해 떨어지게 되어 다음과 같이 블럭이 남게 됩니다.
특정 구간의 블럭을 두 번 빼는 과정을 거친 이후의 결과를 출력하는 프로그램을 작성해보세요.

출력
두 번의 블록 빼기 작업을 진행한 이후의 결과를 출력합니다.
첫 번째 줄에는 남은 블록의 개수를 출력합니다.
그 다음 번째 줄 부터는 한 줄에 하나씩 위에서부터 남은 블록에 적힌 숫자들을 순서대로 출력합니다

ex)
1
2
3       1       1
1   ->  1   ->  5
1       5
5

Input
s1, e1 = 2, 4
s2, e2 = 2, 2

Output
2
1
5
"""
# My
import sys
input = sys.stdin.readline

n = int(input())
array = []
for _ in range(n):
    array.append(int(input()))

for _ in range(2):
    s, e = map(int, input().split())
    del array[s - 1:e]

print(len(array))
for i in array:
    print(i)

# My2
import sys
input = sys.stdin.readline

n = int(input())
array = []
for _ in range(n):
    array.append(int(input()))

for _ in range(2):
    s, e = map(int, input().split())
    array = array[:s - 1] + array[e:]

print(len(array))
for i in array:
    print(i)

# Sol
# 변수 선언 및 입력
n = int(input())
numbers = [
    int(input())
    for _ in range(n)
]
end_of_array = n


# 입력 배열에서 지우고자 하는 부분 수열을 삭제합니다.
def cut_array(start_idx, end_idx):
    global end_of_array, numbers

    temp_arr = []

    # 구간 외의 부분만 temp 배열에 순서대로 저장합니다.
    for i in range(end_of_array):
        if i < start_idx or i > end_idx:
            temp_arr.append(numbers[i])

    # temp 배열을 다시 numbers 배열로 옮겨줍니다.
    end_of_array = len(temp_arr)
    for i in range(end_of_array):
        numbers[i] = temp_arr[i]


# 두 번에 걸쳐 지우는 과정을 반복합니다.
for _ in range(2):
    s, e = tuple(map(int, input().split()))
    # [s, e] 구간을 삭제합니다.
    cut_array(s - 1, e - 1)

# 출력:
print(end_of_array)
for i in range(end_of_array):
    print(numbers[i])