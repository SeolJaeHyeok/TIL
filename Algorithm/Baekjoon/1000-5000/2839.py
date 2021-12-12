# 2839
# 1
n = int(input())

count = 0
while n != 0:
    if n < 0:
        count = -1
        break
    if n % 5 == 0:
        count += n // 5
        break
    else:
        n -= 3
        count += 1

if count > 0:
    print(count)
else:
    print(-1)

# 2
N = int(input())
result = 0

while N >= 0:
    if N % 5 == 0:
        result += N // 5
        print(result)
        break
    N -= 3
    result += 1
else:
    print(-1)