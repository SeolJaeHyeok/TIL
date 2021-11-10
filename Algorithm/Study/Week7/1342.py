# 행운의 문자열
# 메모리 초과
from itertools import permutations

s = list(input())
all_p = set(list(permutations(s, len(s))))

count = len(all_p)
for p in all_p:
    for i in range(1, len(p)):
        if p[i] == p[i - 1]:
            count -= 1
            break

print(count)


# DFS 백트래킹, 1336ms
# PyPy3로 제출하니까 통과
import sys

def dfs(depth, string):
    global count, table, charSet
    if depth == len(s):
        count += 1
        return
    for char in charSet:
        idx = ord(char) - ord('a')
        if table[idx] == 0:
            continue
        if string and string[-1] == char:
            continue

        table[idx] -= 1
        dfs(depth + 1, string + char)
        table[idx] += 1

s = list(sys.stdin.readline().rstrip())
count = 0
table = [0] * 26

charSet = set()
for c in s:
    table[ord(c) - 97] += 1
    charSet.add(c)

dfs(0, '')
print(count)

# 3, 2503ms
import sys

def dfs(word, count):
    if count == len(S):
        return 1

    answer = 0
    for key in counter.keys():
        if counter[key] == 0:
            continue
        if word == key:
            continue
        counter[key] -= 1
        answer += dfs(key, count + 1)
        counter[key] += 1

    return answer

S = list(sys.stdin.readline().rstrip())
counter = dict()
for s in S:
    if s in counter:
        counter[s] += 1
    else:
        counter[s] = 1

print(dfs('', 0))
