def solution(n):
    answer = bin(n)[2:] # 입력값의 2진수
    one_count = answer.count('1') # 입력값의 2진수에서 1의 개수

    # 입력값보다 크면서 입력값의 2배 이하의 값을 탐색
    for i in range(n + 1, 2 * n + 1):
        num = bin(i)[2:]  # 2진수로 변환하고
        if num.count('1') == one_count:  # 1의 개수가 같다면
            result = int(bin(i), 2)  # 10진수로 변환하고 탈출
            break

    return result
