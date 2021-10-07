# 5430
from collections import deque

# 1번째 코드 - 시간 초과
# D가 입력되면 항상 큐를 뒤집어서 시간초과 발생 -> 짝수번 뒤집으면 원래와 똑같으므로 홀수번 뒤집었을때만 뒤집기 수행, 이를 위해 뒤집기 횟수를 저장할 변수 선언
def process(func, array):
    # 입력된 문자열 전처리, ex) str:[1,2,3,4] => list:['1','2','3','4']
    result = deque(array)
    # print(array)
    result.popleft()
    result.pop()
    answer = []
    for i in range(len(result)):
        if result[i] != ',':
            answer.append(result[i])

    # 입력된 함수에 따라 수행
    for oper in func:
        # R이 입력되면 배열의 순서의 순자를 뒤집기
        if oper == 'R':
            answer.reverse()
        # D가 입력되면 배열의 첫 번째 요소 제거
        elif oper == 'D':
            if len(answer) > 1:
                answer = answer[1:]
            else:
                answer = 'error'

    return answer


t = int(input())

for i in range(t):
    func = input().upper()
    num_array = int(input())
    data = input()
    result = process(func, data)
    print(result)


# 2번째 코드, sol
def process(func, array, num_array):
    answer = deque(array)
    rev = 0

    # 입력된 배열의 길이가 0일 경우
    if num_array < 1:
        answer = []  # 빈 리스트로 만들기

    # 입력된 함수에 따라 수행
    for oper in func:
        # R이 입력된 경우
        if oper == 'R':
            rev += 1  # 뒤집기 횟수 증가
        # D가 입력된 경우
        elif oper == 'D':
            # 배열의 길이가 0이라면 error 발생
            if len(answer) < 1:
                answer = 'error'
                return answer
            # 뒤집기가 짝수번 일어난 경우 원래의 배열과 똑같으므로 맨 앞의 요소를 제거한다
            if rev % 2 == 0:
                answer.popleft()
            # 뒤집기가 홀수번 일어난 경우 원래의 배열을 뒤집은 것이므로 맨 뒤의 요소를 제거한다
            else:
                answer.pop()

    # 뒤집기 횟수에 따라 다르게 처리
    if rev % 2 == 0:
        answer = ",".join(answer)
    else:
        answer.reverse()
        answer = ",".join(answer)

    return answer


t = int(input())

for i in range(t):
    func = input().upper()
    num_array = int(input())
    data = input()[1:-1].split(",")
    result = process(func, data, num_array)
    # 반환받은 결과에 따라 다르게 출력 - error가 반환되면 그대로 출력 그렇지 않다면 반환 결과에 괄호 추가해서 출력
    print('['+result+']' if result != 'error' else result)


# arr = deque(input()[1:-1].split(","))
# print(arr)
# array = deque(input())
# array.popleft()
# array.pop()
# print(array)
# result = []
# data = ''
# for i in range(len(array)):
#     if array[i] != ',':
#         data += array[i]
#         result.append(data)
#     else:
#         data = ''
# print(result)

# data = input()[1:-1].split(",")
# print(data)

# answer = ['1', '2', '3', '4']
# answer1 = [",".join(answer)]
# answer2 = ",".join(answer)
# print(answer1)
# print(answer2)

