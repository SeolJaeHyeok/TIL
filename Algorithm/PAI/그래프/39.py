# Combination Sum
# 1
def combinationSum(candidates: list, target: int):
    answer = []

    def dfs(csum, index, path):
        # 목표값을 초과한 경우 종료
        if csum < 0:
            return

        if csum == 0:
            answer.append(path)
            return

        # 자신부터 하위 원소 까지의 나열 재귀 호출
        for i in range(index, len(candidates)):
            dfs(csum - candidates[i], i, path+[candidates[i]])

    dfs(target, 0, [])
    return answer

print(combinationSum([2,3,6,7], 7))


# 2
def combinationSum(candidates: list, target: int):
    answer = []

    def dfs(csum, index, path):
        # 목표값을 초과한 경우 종료
        if csum > target:
            return

        if csum == target:
            answer.append(path)
            return

        # 자신부터 하위 원소 까지의 나열 재귀 호출
        for i in range(index, len(candidates)):
            dfs(csum + candidates[i], i, path+[candidates[i]])

    dfs(0, 0, [])
    return answer

print(combinationSum([2,3,6,7], 7))