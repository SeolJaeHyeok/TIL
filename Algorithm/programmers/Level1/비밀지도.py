# 2018 카카오 블라인드 테스트 [1차] 비밀 지도
def solution(n, arr1, arr2):
    answer = []
    first = []
    second = []

    # 첫 번째 배열 2진수로 전처리
    for i in range(len(arr1)):
        first.append(bin(arr1[i])[2:])

    for i in range(len(first)):
        if len(first[i]) != n:
            first[i] = '0' * (n - len(first[i])) + first[i]

    # 두 번째 배열 2진수로 전처리
    for i in range(len(arr2)):
        second.append(bin(arr2[i])[2:])

    for i in range(len(second)):
        if len(second[i]) != n:
            second[i] = '0' * (n - len(second[i])) + second[i]

    for i in range(n):
        tmp = ''
        for j in range(n):
            if first[i][j] == '0' and second[i][j] == '0':
                tmp += ' '
            else:
                tmp += '#'
        answer.append(tmp)

    return answer