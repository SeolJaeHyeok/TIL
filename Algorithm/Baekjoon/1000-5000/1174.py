import sys
input = sys.stdin.readline

n = int(input())
array = []

def dfs(cur):
    # 해당 숫자를 리스트에 추가한 후
    array.append((int(cur)))
    # 현재 입력된 수보다 작은 숫자를 뒤에 추가
    for i in range(int(cur[-1])):
        dfs(cur + str(i))

# 각 자리로 시작하는 모든 경우의 수를 탐색
for i in range(10):
    dfs(str(i))

array.sort()

if n >= 1024: # 987654210까지 모두 구하면 총 1023개
    print(-1)
else:
    print(array[n - 1])