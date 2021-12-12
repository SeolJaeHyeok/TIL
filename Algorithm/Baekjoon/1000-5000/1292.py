# 쉽게 푸는 문제
# 모든 요소 배열에 추가
def solution(s, e):
    array = []
    # 1~1000까지 해당 숫자(i)의 개수만큼 해당 숫자를 배열에 추가
    for i in range(1, 1001):
        for j in range(1, i+1):
            array.append(i)

    # 이 방법이 훨씬 빠름
    # for i in range(1, 10):
    #     array += [i] * i

    # 구간 합 반환
    return sum(array[s - 1:e])


start, end = map(int, input().split())
print(solution(start, end))
