import sys
import math
input = sys.stdin.readline

a, b = map(int, input().split())
# 두 수의 곱을 두 수의 최대 공약수로 나누면 두 수의 최소 공배수가 된다.
print(a * b // math.gcd(a, b))