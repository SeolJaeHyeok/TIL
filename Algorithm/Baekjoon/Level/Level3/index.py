# 2739번
num = int(input())
for i in range(1,10):
    print('{} * {} = {}'.format(num, i, num*i))

# 10950번
T = int(input())
result = []
for i in range(T):
    num1, num2 = map(int, input().split())
    result.append(num1+num2)

for i in result:
    print(i)

# 8393번
num = int(input())

for i in range(num):
    num += i

print(num)

# 15552번
import sys
T = int(sys.stdin.readline())
for i in range(T):
    a, b = map(int, sys.stdin.readline().split())
    print(a + b)

# 2741번
num = int(input())
for i in range(num):
    print(i+1)

# 2742번
num = int(input())
for i in range(num, 0, -1):
    print(i)

# 11021번
T = int(input())
for i in range(T):
    a, b = map(int, input().split())
    print('Case #{}: {}'.format(i+1, a+b))

# 11022번
T = int(input())
for i in range(T):
    a, b = map(int, input().split())
    print('Case #{}: {} + {} = {}'.format(i+1, a, b, a+b))

# 2438번
# 1
N = int(input())

for i in range(1, N+1):
     print(i*'*')

# 2
N = int(input())
for i in range(1, N+1):
    for j in range(i):
        print('*', end='')
    print('')

# 2439번
# 1
N = int(input())
for i in range(1, N+1):
    for j in range(i):
        result = '*'*i
    print(result.rjust(5))

# 2
N = int(input())
for i in range(1, N+1):
     print(' '*(N-i)+'*'*i)

# 10871번
# 1
N, X = map(int, input().split())
result = []
for i in range(N):
    A = int(input())
    if A < X:
        result.append(A)

for j in result:
    print(j, end=' ')

# 2
N, X = map(int, input().split())
A = list(map(int, input().split()))
for i in range(N):
    if A[i] < X:
        print(A[i], end=" ")
