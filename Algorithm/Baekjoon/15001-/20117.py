import sys
input = sys.stdin.readline

def cal(arr):
    n = len(arr)
    if len(arr) % 2 == 0:
        return arr[n // 2] * n


n = int(input())
array = list(map(int, input().split()))
array.sort()

max_money = 0
if n % 2 == 0:
    for i in range(n // 2):
        target = cal([array[i], array[n - i - 1]])
        max_money += target
else:
    max_money = array[n // 2]
    for i in range(n // 2):
        target = cal([array[i], array[n - i - 1]])
        max_money += target

print(max_money)