import sys, math
input = sys.stdin.readline

# 소수 판별
def isPrime(n):
    if n == 1:
        return False
    if n == 2 or n == 3:
        return True
    for i in range(2, math.ceil(math.sqrt(n)) + 2):
        if n % i == 0:
            return False
    return True

n = int(input())

answer = 0
for i in range(n, 1000001):
    # 팰린드롬 판별
    if str(i) == str(i)[::-1]:
        if isPrime(i):
            answer = i
            break

if answer == 0:
    print(1003001)
else:
    print(answer)

