# 10818번
# 1
# N = int(input())
# nums = list(map(int, input().split()))
# nums.sort()
# print(nums[0], nums[-1])

# 2562번
# 1
# nums = []
# maxNum = 0
# maxNumIdx = 0
# for i in range(9):
#     num = int(input())
#     nums.append(num)
#
# for j in range(len(nums)):
#     if nums[j] > maxNum:
#         maxNum = nums[j]
#         maxNumIdx = j
#
# print('{}\n{}'.format(maxNum, maxNumIdx + 1))

# 2
# nums = []
# for i in range(9):
#     num = int(input())
#     nums.append(num)
#     maxNum = max(nums)
#     maxNumIdx = nums.index(maxNum)
#
# print('{}\n{}'.format(maxNum, maxNumIdx + 1))

# 2577번
# 1
# A = int(input())
# B = int(input())
# C = int(input())
# multipliedResult = list(str(A * B * C))
# resultTable = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# Output = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#
# for i in range(len(multipliedResult)):
#     for j in range(len(resultTable)):
#         if int(multipliedResult[i]) == resultTable[j]:
#             Output[j] += 1
# for result in Output:
#     print(result)

# 2
# A = int(input())
# B = int(input())
# C = int(input())
#
# mul = str(A*B*C)
# result = [0] * 10
#
# for i in range(len(mul)):
#     result[int(mul[i])] += 1
#
# for i in range(10):
#     print(result[i])

# 3052번
# 1
# lst = []
#
# for i in range(10):
#     num = int(input())
#     lst.append(num % 42)
#
# print(len(set(lst)))  # 집합 자료형 {} 은 중복을 허용하지 않기 때문에 서로 다른 수를 구할 때 용이

# 2
# lst = []
#
# for i in range(10):
#     num = int(input()) % 42  # 42로 나눈 나머지 값이
#     if not num in lst:  # 리스트 안에 없으면 추가 == 중복된 요소가 없으면 추가
#         lst.append(num)
#
# print(len(lst))
print('Testing')
