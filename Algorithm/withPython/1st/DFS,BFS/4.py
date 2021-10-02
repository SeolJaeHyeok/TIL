# 연산자 끼워 넣기

n = int(input())
data = list(map(int, input().split()))

add, sub, mul, div = map(int, input().split())
max_value = -1e9
min_value = 1e9

def dfs(i, now):
    global max_value, min_value, add, sub, mul, div
    if i == n:
        max_value = max(max_value, now)
        min_value = min(min_value, now)
    else:
        if add > 0:
            add -= 1
            dfs(i + 1, now + data[i])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(i + 1, now - data[i])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(i + 1, now * data[i])
            mul += 1
        if div > 0:
            div -= 1
            dfs(i + 1, int(now / data[i]))
            div += 1

dfs(1, data[0])

print(max_value)
print(min_value)


# 백트래킹
n = int(input())
data = list(map(int, input().split()))

add, sub, mul, div = map(int, input().split())
max_value = -1e9
min_value = 1e9


def dfs(cnt, result, add, sub, mul, div):
    global max_value
    global min_value
    if cnt == n:
        max_value = max(max_value, result)
        min_value = min(min_value, result)
        return
    if add:
        dfs(cnt + 1, result + data[cnt], add - 1, sub, mul, div)
    if sub:
        dfs(cnt + 1, result - data[cnt], add, sub - 1, mul, div)
    if mul:
        dfs(cnt + 1, result * data[cnt], add, sub, mul - 1, div)
    if div:
        dfs(cnt + 1, -(-result // data[cnt]) if result < 0 else result // data[cnt], add, sub, mul, div - 1)


dfs(1, data[0], add, sub, mul, div)
print(max_value)
print(min_value)