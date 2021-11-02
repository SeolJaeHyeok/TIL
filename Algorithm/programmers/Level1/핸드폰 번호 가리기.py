def solution(phone_number):
    answer = '*' * (len(phone_number) - 4) + phone_number[-4:]

    return answer


def solution(phone_number):
    answer = ''
    for i in range(len(phone_number) - 4):
        answer += '*'
    for j in range(len(phone_number) - 4, len(phone_number)):
        answer += phone_number[j]

    return answer
