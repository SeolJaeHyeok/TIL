# Permutations
# itertools 모듈 이용
from itertools import permutations

# def permute(nums:list):
#     return list(map(list, permutations(nums)))
#
# print(permute([1, 2, 3]))

# dfs 이용
def permute(nums:list):
    result = []
    prev_elements = []

    def dfs(elements):
        if len(elements) == 0:
            result.append(prev_elements[:])
            return

        for e in elements:
            # 자기 자신을 제외한 모든 요소
            next_elements = elements[:]
            next_elements.remove(e)

            prev_elements.append(e)
            dfs(next_elements)
            prev_elements.pop()

    dfs(nums)
    return result


print(permute([1, 2, 3]))
