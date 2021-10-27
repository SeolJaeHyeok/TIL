# Combinations
# 1
def combine(n: int, k: int):
    result = []
    def dfs(elements, start, k):
        if k == 0:
            result.append(elements[:])
            return

        # 자신 이전의 모든 값을 고정하여 재귀 호출
        for i in range(start, n + 1):
            elements.append(i)
            dfs(elements, i + 1, k - 1)
            elements.pop()

    dfs([], 1, k)
    return result

print(combine(4, 2))

# 2
def combine(n: int, k: int):
    result = []
    li = [i for i in range(1, n + 1)]
    def dfs(elements, start, k):
        if k == 0:
            result.append(elements[:])
            return

        # 자신 이전의 모든 값을 고정하여 재귀 호출
        for i in range(start, n):
            dfs(elements + [li[i]], i + 1, k - 1)

    dfs([], 0, k)
    return result

print(combine(4, 2))


# 3
def combine(n: int, k: int):
    answer = []

    def dfs(index, elements):
        if len(elements) == k:
            answer.append(elements[:])
            return

        for i in range(index, n + 1):
            dfs(i + 1, elements + [i])

    dfs(1, [])

    return answer

print(combine(4, 2))