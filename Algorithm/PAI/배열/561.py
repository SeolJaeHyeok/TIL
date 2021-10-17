# Array Partition
# 정렬 후 계산, O(n), 276ms
def arrayPartition(nums: list):
    nums.sort()
    sum = 0
    for i in range(0, len(nums), 2):
        sum += min(nums[i], nums[i + 1])

    return sum

print(arrayPartition([1, 4, 3, 2]))
print(arrayPartition([1, 7, 6, 2, 5, 4]))

# 짝수 번째 값 계산, 240ms
def arrayPartition(nums: list):
    nums.sort()
    sum = 0
    for i in range(0, len(nums), 2):
        sum += nums[i]

    return sum

print(arrayPartition([1, 4, 3, 2]))
print(arrayPartition([1, 7, 6, 2, 5, 4]))

# Pythonic Way, 260ms
def arrayPartition(nums: list):
    return sum(sorted(nums)[::2])

print(arrayPartition([1, 4, 3, 2]))
print(arrayPartition([1, 7, 6, 2, 5, 4]))