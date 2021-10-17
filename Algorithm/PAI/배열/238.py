# Product of Array Except Self
# 브루트 포스, 시간 초과
def productOfArray(nums: list):
    value = 1
    array = []
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i == j:
                continue
            else:
                value *= nums[j]

        array.append(value)
        value = 1
    return array


print(productOfArray([1, 2, 3, 4]))
print(productOfArray([2, 5, 6, 4]))


# 왼쪽 곱셈 결과에 오른쪽 값을 차례대로 곱셈(1), 240ms
def productOfArray(nums: list):
    array = []
    value = 1
    # 자기 자신을 기준으로 왼쪽에 있는 모든 수의 곱셈
    for i in range(len(nums)):
        array.append(value)
        value *= nums[i]

    value = 1
    # 왼쪽 곱셈 결과에 오른쪽 값을 차례대로 곱셈
    for i in range(len(nums) - 1, -1, -1):
        array[i] = array[i] * value
        value *= nums[i]

    return array


print(productOfArray([1, 2, 3, 4]))
print(productOfArray([2, 5, 6, 4]))


# 왼쪽 곱셈 결과에 오른쪽 값을 차례대로 곱셈(2), 240ms
def productExceptSelf(nums: list):
    # 나눗셈 연산 없이, O(n)의 시간복잡도로 풀어야 한다
    # = "자기 자신을 제외한 왼쪽의 곱셈 결과 * 오른쪽 곱셈 결과" 형태로 값을 구해야 한다.
    # [1,2,3,4] 예시

    # 1. 자기 자신을 기준으로 왼쪽에 있는 값들의 곱셈 결과값 구하기.
    # 왼쪽 첫 번째 숫자는 곱한 값이 없어야 하므로 시작값을 1로 초기화한다.
    n = 1
    left, right = [], []
    for i in range(len(nums)):
        left.append(n)
        n *= nums[i]
    # [곱하지 않은 값, 1번째, 1*2번째, 1*2*3번째] 값이 left에 저장된다.

    n = 1
    for i in range(len(nums) - 1, -1, -1):
        right.append(n)
        n *= nums[i]
    right.reverse()
    # [2*3*4번째, 3*4번째, 4번째, 곱하지 않은 값] 값이 right에 저장된다.

    # left idx값에 right의 idx값을 곱하면 원하는 결과를 얻을 수 있다.
    for idx in range(len(nums)):
        left[idx] = left[idx] * right[idx]

    return left
