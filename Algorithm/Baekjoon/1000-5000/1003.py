import sys
input = sys.stdin.readline

t = int(input())

def fibonacci(n):
    zero_arr = [1, 0, 1]
    one_arr = [0, 1, 1]
    for i in range(3, n + 1):
        # n번째 수의 나타나는 0과 1의 개수는 n-1번째와 n-2번째 수에서 나타난 0과 1을 합친 수
        zero_arr.append(zero_arr[i - 1] + zero_arr[i - 2])
        one_arr.append(one_arr[i - 1] + one_arr[i - 2])

    print(zero_arr[n], one_arr[n])

for _ in range(t):
    num = int(input())
    fibonacci(num)
