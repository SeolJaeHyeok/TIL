"""
직사각형의 대각선이 지나는 격자점 및 대각선에 의해 잘려지는 사각형
- 직사각형의 양 끝점을 제외한 내부의 격자점의 개수는 (가로, 세로의 최대 공약수 - 1)
- 대각선에 의해 잘려지는 사각형은 (가로 + 세로 - 최대 공약수)
https://m.blog.naver.com/orbis1020/220664563768
"""


# 최대 공약수 구하는 방법
# 함수 이용
def gcd_func(x, y):
    while y:
        # print(x, y)
        x, y = y, x % y
        # print(x, y)

    return x


print(gcd_func(12, 8))
print(gcd_func(10, 23))
print(gcd_func(16, 4))
print(gcd_func(12, 75))
print()

# 라이브러리 이용
from math import gcd

print(gcd(12, 8))
print(gcd(10, 23))
print(gcd(16, 4))
print(gcd(12, 75))