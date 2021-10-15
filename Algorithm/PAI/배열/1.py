# Two Sum
# 브루트 포스로 모든 경우 탐색, O(n^2), 4093ms
def twoSum(nums: list, target: int):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


result = twoSum([1, 2, 3, 6, 11, 7, 15], 12)
print(result)


# in 을 이용한 탐색, 652ms
def twoSum(nums: list, target: int):
    for i, n in enumerate(nums):
        complement = target - n  # 첫 번째 값을 뺀 나머지 값

        # 위 값이 배열 안에 존재할 경우
        if complement in nums[i + 1:]: # 배열을 탐색할 때 시작값 이후의 배열들을 탐색해야 한다.
            # return [nums.index(n), nums.index(complement)] -> [3, 3], 6일 경우 예외
            return [nums.index(n), nums[i + 1:].index(complement) + (i + 1)]


result = twoSum([1, 2, 3, 6, 11, 7, 15], 12)
print(result)

# 첫 번째 수를 뺸 결과 키 조회, 비교 탐색 대신 딕셔너리로 한 번에 값 찾기, 125ms
def twoSum(nums: list, target: int):
    nums_map = {}
    # 키와 값을 바꿔서 딕셔너리로 저장
    for i, num in enumerate(nums):
        nums_map[num] = i

    # 타겟에서 첫 번째 수를 뺀 결과를 키로 조회
    for i, num in enumerate(nums):
        if target - num in nums_map and i != nums_map[target - num]:
            return [nums.index(num), nums_map[target - num]]


result = twoSum([1, 2, 3, 6, 11, 17, 15], 12)
print(result)

# 위 방법을 하나의 for 문으로 통일
def twoSum(nums: list, target: int):
    nums_map = {}
    for i, num in enumerate(nums):
        if target - num in nums_map:
            return [nums_map[target - num], i]
        nums_map[num] = i


result = twoSum([1, 2, 3, 6, 11, 7, 15], 12)
print(result)

# 투 포인터 풀이
# 하지만 투 포인터 풀이를 하기 위해서는 nums 배열이 정렬되어 있어야 한다.
# 정렬을 시킨다면 인덱스가 모두 엉망이 되기 때문에 정확한 요구사항을 구현할 수가 없게 된다.
def twoSum(nums: list, target: int):
    nums.sort()
    left, right = 0, len(nums) - 1
    while not left == right:
        if nums[left] + nums[right] > target:
            right -= 1
        elif nums[left] + nums[right] < target:
            left -= 1
        else:
            return [left, right]

result = twoSum([1, 2, 3, 6, 11, 7, 15], 12)
print(result)