import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = []

for _ in range(n):
    g, x = map(int, input().split())
    arr.append((g, x))

table = [0] * 1000001

for i in range(len(arr)):
    table[arr[i][1]] = arr[i][0]

window_range = 2 * k + 1 # 고정된 윈도우의 범위
window_sum = sum(table[:window_range]) # 첫 윈도우의 합
answer = window_sum

for i in range(window_range, 1000001):
    window_sum += (table[i] - table[i - window_range])
    answer = max(answer, window_sum)

print(answer)