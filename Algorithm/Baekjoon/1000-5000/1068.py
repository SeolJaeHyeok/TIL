import sys
input = sys.stdin.readline
CONST = 1e9

def dfs(num, arr):
    arr[num] = CONST
    for i in range(len(arr)):
        if num == arr[i]:
            dfs(i, arr)

n = int(input())
nodes = list(map(int, input().split()))
target = int(input())

dfs(target, nodes)

count = 0
for i in range(len(nodes)):
    if nodes[i] != CONST and i not in nodes:
        count += 1

print(count)