# 애너그램, 1.5hours
# 2, 메모리 초과
import sys
from itertools import permutations

n = int(sys.stdin.readline())

for _ in range(n):
    word = sys.stdin.readline().rstrip()
    array = set(list(permutations(word, len(word))))
    answer = sorted(list(array))
    for a in answer:
        print(''.join(a))


# 2, 순열 구현 -> 메모리 초과
import sys

def permute(words:list):
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

    dfs(words)
    return result


n = int(sys.stdin.readline())
for _ in range(n):
    words = list(sys.stdin.readline().rstrip())
    array = permute(words)
    answer = set()
    for a in array:
        answer.add(''.join(a))

    for word in sorted(answer):
        print(word)


# 3, 백트래킹, 통과
import sys
from collections import defaultdict

def dfs(depth):
    if depth == len(words):
        print(''.join(answer))
        return
    # 백트래킹
    for c in counter:
        if counter[c]:
            counter[c] -= 1
            answer[depth] = c
            dfs(depth + 1)
            counter[c] += 1


n = int(sys.stdin.readline())
for _ in range(n):
    words = sorted((sys.stdin.readline().rstrip()))
    answer = [0] * len(words)

    counter = defaultdict(int)
    for char in words:
        counter[char] += 1

    dfs(0)
