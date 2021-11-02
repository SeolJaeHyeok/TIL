def solution(n):
    array = list(str(n))
    array.reverse()
    answer = []
    for num in array:
        answer.append(int(num))

    return answer

def solution(n):
    return list(map(int, list(str(n))[::-1]))