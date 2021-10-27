# Subsets
def subsets(nums: list):
    answer = []

    def bfs(index, path):
        # 매번 결과 추가
        answer.append(path)

        # 경로 만들면서 재귀 호출
        for i in range(index, len(nums)):
            bfs(i + 1, path + [nums[i]])

    bfs(0, [])
    return answer

print(subsets([1,2,3]))