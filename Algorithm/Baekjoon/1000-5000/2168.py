# 타일 위의 대각선
# 1, 최대 공약수 라이브러리 이용
from math import gcd

x, y = map(int, input().split())
g = gcd(x, y)

print(x + y - g)

# 2, 최대 공약수 함수 구현
def gcd(x, y):
    while y:
        # print(x, y)
        x, y = y, x % y
        # print(x, y)

    return x

x, y = map(int, input().split())
g = gcd(x, y)

print(x + y - g)
"""
직사각형의 대각선이 지나는 격자점 및 대각선에 의해 잘려지는 사각형
- 직사각형의 양 끝점을 제외한 내부의 격자점의 개수는 (가로, 세로의 최대 공약수 - 1)
- 대각선에 의해 잘려지는 사각형은 (가로 + 세로 - 최대 공약수)
출처 - https://m.blog.naver.com/orbis1020/220664563768
"""
