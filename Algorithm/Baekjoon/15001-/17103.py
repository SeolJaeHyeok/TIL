import sys, math
input = sys.stdin.readline

# 1, 시간 초과

# n 이하의 소수를 모두 반환하는 함수
def isPrime(n):
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

t = int(input())

for _ in range(t):
    n = int(input())
    arr = isPrime(n)
    count = 0
    # n 이하의 소수를 완전 탐색
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if arr[i] + arr[j] == n:
                count += 1

    print(count)


# 2, 시간 초과
def isPrime(n):
    if n == 1:
        return False
    if n == 2 or n == 3:
        return True
    for i in range(2, math.ceil(math.sqrt(n)) + 2):
        if n % i == 0:
            return False
    return True

t = int(input())
nums = [int(input()) for _ in range(t)]
prime_array = []

for i in range(max(nums)):
    prime_array.append(isPrime(i))

for num in nums:
    count = 0

    for i in range(2, num // 2 + 1):
        if prime_array[i] and prime_array[num - i]:
            count += 1

    print(count)


# 3
def isPrime(n):
    array = [1 for _ in range(n+1)]

    for i in range(2, int(n ** 0.5) + 1):
        if array[i]:
            j = 2

        while i * j <= n:
            array[i * j] = 0
            j += 1

    return array

T = int(input())
nums = [int(input()) for _ in range(T)]
max_num = max(nums)
prime_array = isPrime(max_num)

for num in nums:
    result = 0

    for i in range(2, num // 2 + 1):
        if prime_array[i] and prime_array[num - i]:
            result += 1

    print(result)



