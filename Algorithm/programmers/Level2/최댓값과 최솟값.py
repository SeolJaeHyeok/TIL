def solution(s):
    s = s.split(' ')
    result = []
    for i in s:
        result.append(int(i))
    max_value = max(result)
    min_value = min(result)
    answer = str(min_value) + ' ' + str(max_value)

    return answer