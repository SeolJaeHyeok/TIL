def solution(new_id):
    step1 = new_id.lower()  # 1단계

    # 2단계
    step2 = ''
    for char in step1:
        if char.isalnum() or char == '-' or char == '_' or char == '.':
            step2 += char

    # 3단계
    answer = step2[0]
    for i in range(1, len(step2)):
        if step2[i-1] == '.' and step2[i] == '.':
            continue
        answer += step2[i]

    # 4단계
    if answer[0] == '.' and answer[-1] == '.':
        answer = answer[1:-1]
    elif answer[0] == '.' and answer[-1] != '.':
        answer = answer[1:]
    elif answer[-1] == '.' and answer[0] != '.':
        answer = answer[:-1]

    # 5단계
    if len(answer) == 0:
        answer = 'a'

    # 6단계
    if len(answer) > 15:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]

    # 7단계
    if len(answer) <= 2:
        while len(answer) < 3:
            answer += answer[-1]

    return answer

# 불필요한 로직 개선
def solution(new_id):
    step1 = new_id.lower()  # 1단계

    # 2단계
    answer = ''
    for char in step1:
        if char.isalnum() or char in ['-', '_', '.']:
            answer += char

    # 3단계
    while '..' in answer:
        answer = answer.replace('..', '.')

    # 4단계
    if answer[0] == '.':
        answer = answer[1:] if len(answer) > 1 else '.'
    if answer[-1] == '.':
        answer = answer[:-1]

    # 5단계
    if len(answer) == 0:
        answer = 'a'

    # 6단계
    if len(answer) > 15:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]

    # 7단계
    while len(answer) < 3:
        answer += answer[-1]

    return answer