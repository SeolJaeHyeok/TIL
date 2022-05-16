import sys
import math
import itertools
import collections

# 이진 검색을 이용한 list.find(x)
def bin_search(l, x):
    left = 0
    right = len(l)
    mid = right//2
    while (left + 1) < right:
        if l[mid] > x:
            right = mid
        else:
            left = mid
        mid = (left + right) // 2
    if l[mid] == x:
        return mid
    else:
        return -1

# 빠른 unsigned int 입력
def cin():
    r = 0
    while True:
        x = sys.stdin.read(1)
        if x == ' ' or x == '\n':
            return r
        r *= 10
        r += int(x)

# 파스칼의 삼각형을 이용한 nCk 또는 이항계수
def combi_pascal(n, k):
    if k > (n - k):
        k = n - k
    l = [[1], [1, 1]]
    for i in range(2, n + 1):
        l.append([1])
        for j in range(1, i + 1):
            if j == i:
                l[i].append(1)
            else:
                l[i].append(l[i - 1][j - 1] + l[i - 1][j])
    return l[n][k]

# 단순연산을 통한 팩토리얼
def fact(n):
    r = 1
    for i in range(2, n + 1):
        r *= i
    return r

# 변수 2개만 이용한 피보나치
def fib_dp_memopt(n):
    if n == 1 or n == 2:
        return 1
    a, b = 1, 1
    for _ in range(n-2):
        a, b = b, a + b
    return b

# 재귀를 이용한 피보나치
def fib_recursive(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib_recursive(n - 1) + fib_recursive(n - 2)

# 유클리드 호제법
def gcd1(a, b):
    if a == 0:
        return b
    return gcd1(b % a, a)

def gcd2(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd2(a, b)


# sqrt(n) 이하의 홀수로 나눠보는 전통적인 소수 판별 함수
def isprime_sqrt(n):
    if n == 1:
        return False
    if n == 2 or n == 3:
        return True
    for i in range(2, math.ceil(math.sqrt(n)) + 2):
        if n % i == 0:
            return False
    return True


# 에라토스테네스의 체를 개량하여 n 이하의 소수를 전부 반환
def isprime_sieve(n):
    p = [None, None, True, True] + [False, True] * (n // 2 - 1)
    l = []
    x = math.ceil(math.sqrt(n))
    for i in range(3, x + 1, 2):
        if p[i]:
            for j in range(i * 3, n + 1, i * 2):
                p[j] = False
            l.append(i)
    for i in range(x - x % 2 + 1, n + 1, 2):
        if p[i]:
            l.append(i)
    return l

# 에라토스테네스의 체를 더 빠르고 가볍게 개량하여 n 이하의 소수를 전부 반환
def isprime_sieve_memopt(n):
    root = int(math.sqrt(n))
    if root % 2 == 0:
        root += 1
    sieve = [None] * (n // 2 + 2)
    ret = [2]
    for i in range(1, (root + 1) // 2):
        if not sieve[i]:
            ret.append(2 * i + 1)
            t = 2 * i + 1
            for j in range((t * t) // 2, n // 2 + 1, t):
                sieve[j] = True
    for i in range((root + 1) // 2, n // 2 + 1):
        if not sieve[i]:
            ret.append(2 * i + 1)
    if ret[-1] > n:
        return ret[:-1]
    return ret

# A진법 수 a를 10진법을 거쳐 B진법 수 리스트로 변환
def jin(A, a, B):
    x = 0
    if type(a) == int:
      t = []
      while a:
        n, m = divmod(a, A)
        t.append(m)
        a = t[::-1]
    for i in range(len(a)):
        x += a[-i - 1] * A ** i
    b = []
    while x:
        x, m = divmod(x, B)
        b.append(m)
    return b[::-1]

# 양수의 자릿수
def nlen(n):
    d = 0
    while n != 0:
        n //= 10
        d += 1
    return d

# 고1 수학의 nCr(조합)
def combi(n, r):
    return fact(n) // fact(r) // fact(n - r)

# 고1 수학의 nPr(순열)
def permu(n, r):
    return fact(n) // fact(r)

# 카탈란 수
def catalan(n):
    return fact(2 * n) // fact(n + 1) // fact(n)
