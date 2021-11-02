def solution(n):
    array = list(str(n))

    array.sort(reverse=True)

    return int(''.join(array))