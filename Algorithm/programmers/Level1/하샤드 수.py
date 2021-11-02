def solution(number):
    answer = 0
    for num in str(number):
        answer += int(num)

    return True if number % answer == 0 else False