# 연산자 끼워넣기(2)
# 백트래킹으로 모든 경우 탐색
def dfs(idx, num):
    global max_value, min_value, add, sub, mul, div

    # n-1번 연산이 수행됐으면(모든 연산 완료) 최대, 최소값 갱신
    if idx == n:
        max_value = max(max_value, num)
        min_value = min(min_value, num)
        return
    else:
        if add > 0:
            add -= 1
            dfs(idx + 1, num + nums[idx])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(idx + 1, num - nums[idx])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(idx + 1, num * nums[idx])
            mul += 1
        if div > 0:
            div -= 1
            dfs(idx + 1, int(num / nums[idx]))
            div += 1

n = int(input())
nums = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

max_value = -1e9
min_value = 1e9

dfs(1, nums[0])
print(max_value)
print(min_value)





