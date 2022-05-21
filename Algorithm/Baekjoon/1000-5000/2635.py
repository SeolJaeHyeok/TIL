import sys
input = sys.stdin.readline
num = int(input())

arr = []

for i in range(num // 2, num + 1):
    tmp_arr = []
    tmp_arr.append(num) # 첫 번째 수
    tmp_arr.append(i) # 두 번째 수
    # 수 이어가기
    while tmp_arr[-1] >= 0:
        tmp_arr.append(tmp_arr[-2] - tmp_arr[-1])

    # 정답 갱신
    if len(tmp_arr) >= len(arr):
        arr = tmp_arr

print(len(arr) - 1)
print(*arr[:-1])