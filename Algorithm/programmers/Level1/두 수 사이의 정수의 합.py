def solution(a, b):
    answer = 0
    x = min(a, b)
    y = max(a, b)
    if x == y:
        return x
    else:
        return sum(range(x, y + 1))

# 등차수열의 합 공식
def solution(a, b):
    return (abs(a-b)+1)*(a+b)//2