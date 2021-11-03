def solution(arr, divisor):
    answer = []
    for num in arr:
        if num % divisor == 0:
            answer.append(num)

    return sorted(answer) if len(answer) > 0 else [-1]


def solution(arr, divisor):
    return sorted([n for n in arr if n % divisor == 0]) or [-1]
