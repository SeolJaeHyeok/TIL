# 1이 될때까지
# my
n, k = map(int, input().split())
count = 0

while True:
    if n == 1:
        break

    if n % k == 0:
        n //= k
        count += 1
    else:
        n -= 1
        count += 1

print(count)

# sol1
n, k = map(int, input().split())
result = 0

# N이 K 이상이라면 K로 계속 나누기
while n >= k:
    while n % k != 0:
        n -= 1
        result += 1
    n //= k
    result += 1

# 마지막으로 남은 수에 대하여 1씩 빼기
while  n > 1:
    n -= 1
    result += 1

print(result)

# sol2
n, k = map(int, input().split())
result = 0

while True:
    # (N == K로 나누어 떨어지는수)가 될 때까지 1씩 빼기
    target = (n // k) * k
    result += (n - target)
    n = target
    # N이 K보다 작을 때(더 이상 나눌 수 없을 때) 반복문 탈출
    if n < k:
        break
    # K로 나누기
    result += 1
    n //= k

result += (n - 1)
print(result)