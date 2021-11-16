# 시간 초과
import sys
from itertools import permutations

t = int(sys.stdin.readline())

for _ in range(t):
    word = sys.stdin.readline().rstrip()
    array = sorted(set(permutations(word, len(word))))
    flag = True
    idx = 0
    while flag:
        for i in range(len(array)):
            target = ''.join(array[i])
            if target == word:
                flag = False
                idx = i

    if idx < len(array) - 1:
        print(''.join(array[idx + 1]))
    else:
        print(''.join(array[-1]))


# C++의 next_permutation 함수 구현
import sys

def next_permutation(arr):
    i = len(arr) - 2
    while i >= 0 and arr[i] >= arr[i + 1]:
        i -= 1
    if i == -1:
        return False

    j = len(arr) - 1
    while arr[i] >= arr[j]:
        j -= 1

    arr[i], arr[j] = arr[j], arr[i]
    result = arr[:i + 1]
    result.extend(list(reversed(arr[i + 1:])))

    return result

t = int(sys.stdin.readline())

for _ in range(t):
    word = list(sys.stdin.readline().rstrip())
    answer = next_permutation(word)
    if answer:
        print(''.join(answer))
    else:
        print(''.join(word))