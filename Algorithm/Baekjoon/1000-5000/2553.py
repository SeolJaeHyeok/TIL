import math
import sys
input = sys.stdin.readline

n = int(input())
num = list(str(math.factorial(n)))

for i in range(len(num) - 1, -1, -1):
    if num[i] != '0':
        print(num[i])
        break
