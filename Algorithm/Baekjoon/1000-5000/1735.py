import sys
import math
input = sys.stdin.readline

x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())

a = (x1 * y2) + (x2 * y1)
b = y1 * y2

gcd = math.gcd(a, b)
print(a//gcd, b//gcd)

