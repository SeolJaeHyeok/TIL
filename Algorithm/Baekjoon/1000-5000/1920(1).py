import sys
input = sys.stdin.readline

n = int(input())
d = [0] * 100001
arr1 = list(map(int, input().split()))
m = int(input())
arr2 = list(map(int, input().split()))

arr1.sort()

def binary_search(target):
    left, right = 0, len(arr1) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr1[mid] == target:
            return True
        elif arr1[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return False

for b in arr2:
    if binary_search(b):
        print(1)
    else:
        print(0)
