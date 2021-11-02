def solution(x, n):
    answer = []
    tmp = x
    for i in range(n):
        answer.append(tmp)
        tmp += x

    return answer