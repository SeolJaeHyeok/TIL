def solution(n):
    answer = 0
    array = list(str(n))
    for num in array:
        answer += int(num)

    return answer

def solution(n):
    return sum([int(i) for i in list(str(n))])