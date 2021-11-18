from math import gcd


def solution(w, h):
    # 가능한 최대 정사각형 개수
    total = w * h
    # 양 꼭짓점을 그었을 때 잘려지는 사각형의 개수 = 가로 + 세로 - 가로, 세로의 최대 공약수
    cut = w + h - gcd(w, h)
    
    return total - cut