# 순열
# 풀이 실패.. https://js1jj2sk3.tistory.com/39 참조하여 제출

# 라이브러리 이용, 메모리 초과
from itertools import permutations


while True:
    try:
        data, target = map(str, input().split())
    except:
        break
    a = list(permutations(data))

    if int(target) >= f:
        print(f'{data} {target} = No permutation')
        continue
    answer = ''.join(a[int(target)-1])
    print(f'{data} {target} = {answer}')


# 순열 구현, 시간 초과
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


while True:
    try:
        data, target = map(str, input().split())
    except:
        break
    nums = list(data)
    a = list(permute(nums))
    f = 1
    for i in range(len(a)):
        f *= i + 1
    if f <= len(a):
        print(f'{data} {target} = No permutation')
    else:
        answer = ''.join(a[int(target)-1])
        print(f'{data} {target} = {answer}')


import sys
sys.stdin = open('input.txt', 'r')

def factorial(n):
    r = 1
    for i in range(1, n + 1):
        r *= i
    return r


def permutations(selected, i):
    global count
    if i == len(s):
        count += 1
        if count == k:
            return selected
    else:
        for c in s:
            if c not in selected:
                r = permutations(selected + c, i + 1)
                if r:
                    return r


while True:
    try:
        s, k = input().split()
    except:
        break
    k = int(k)
    l = factorial(len(s))
    count = 0
    state = False
    answer = permutations('', 0)
    if k > l:
        print(f'{s} {k} = No permutation')
    else:
        print('{} {} = {}'.format(s, k, permutations('', 0)))
