# 3Sum
# 브루트 포스(1), O(n^3), 시간 초과
def threeSum(nums: list):
    nums.sort()
    array = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                if nums[i] + nums[j] + nums[k] == 0:
                    element = [nums[i], nums[j], nums[k]]
                    if element not in array:
                        array.append(element)

    return array

result = threeSum([-1, 0, 1, 2, -1, -4])
print(result)

# 브루트 포스(2), O(n^3), 시간 초과
def threeSum(nums: list):
    nums.sort()
    array = []
    for i in range(len(nums) - 2):
        # 중복된 값 건너 뛰기
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        for j in range(i + 1, len(nums) - 1):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            for k in range(j + 1, len(nums)):
                if k > j + 1 and nums[k] == nums[k - 1]:
                    continue
                if nums[i] + nums[j] + nums[k] == 0:
                    element = [nums[i], nums[j], nums[k]]
                    array.append(element)
    return array

result = threeSum([-1, 0, 1, 2, -1, -4])
print(result)

# 투 포인터로 합 계산, O(n^2), 852ms
def threeSum(nums: list):
    nums.sort()
    array = []
    for i in range(len(nums) - 2):
        # 중복된 값 건너 뛰기
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        # 간격을 좁혀가면 합 계산
        left, right = i + 1, len(nums) - 1
        while left < right:
            value = nums[i] + nums[left] + nums[right]
            if value < 0:
                left += 1
            elif value > 0:
                right -= 1
            else:
                # 합이 0인 경우 정답 처리
                array.append([nums[i], nums[left], nums[right]])

                # 각각의 투 포인터 옆의 값이 동일한 값이 아닐때까지 스킵
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                # 정답을 처리한 후 투 포인터 이동
                left += 1
                right -= 1

    return array


result = threeSum([-1, 0, 1, 2, -1, -4])
print(result)