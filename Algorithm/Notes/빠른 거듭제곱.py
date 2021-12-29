# 고속 거듭제곱
"""
a 의 n승 을 구하기 위해서,
1. **이나 pow()를 사용하면 시간복잡도는 O(n)이다.
2. 고속 거듭제곱 알고리즘을 사용하면 시간복잡도는 O(logN)이다.

제곱의 제곱을 곱해주면서 곱하기의 수를 대폭 줄일 수 있다.
참고: https://blog.naver.com/PostView.nhn?blogId=cjsencks&logNo=221783247166
"""
def power(a, b, m):
    result = 1
    while b > 0:
        if b % 2 != 0:
            result = (result * a) % m
        b //= 2
        a = (a * a) % m

    return result