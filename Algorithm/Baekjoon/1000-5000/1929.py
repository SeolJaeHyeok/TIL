import sys
import math
input = sys.stdin.readline

# n이하의 모든 소수를 반환하는 함수
def isprime(n):
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

m, n = map(int, input().split())
result = isprime(n)
# m이상 n이하의 소수 출력
for i in result:
    if i < m:
        continue
    print(i)