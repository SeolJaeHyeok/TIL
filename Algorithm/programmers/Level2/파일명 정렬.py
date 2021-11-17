# 2018 카카오 블라인드 테스트 3차 파일명 정렬
# 1, 25/100
def solution(files):
    answer = []
    for file in files:
        head = ''
        num = ''

        # head
        n_idx = 0
        for i in range(len(file)):
            if file[i].isnumeric():
                n_idx = i
                break
            head += file[i]

        # number
        t_idx = 0
        for i in range(n_idx, len(file)):
            if file[i].isnumeric():
                num += file[i]
            else:
                t_idx = i
                break

        # tail
        tail = ''.join(file[t_idx:])
        answer.append((head, num, tail))

    answer.sort(key=lambda x: (x[0].upper(), int(x[1])))

    return [''.join(answer[i]) for i in range(len(answer))]


# 2, 55/100
def solution(files):
    answer = []

    for f in files:
        head, num, tail = '', '', ''
        flag = False
        for i in range(len(f)):
            if f[i].isnumeric():
                num += f[i]
                flag = True
            elif not flag:
                head += f[i]
            else:
                tail += f[i]

        answer.append((head, num, tail))

    answer.sort(key=lambda x: (x[0].upper(), int(x[1])))

    return [''.join(answer[i]) for i in range(len(answer))]


# 3, 100/100
def solution(files):
    answer = []

    for f in files:
        head, num, tail = '', '', ''
        flag = False # number check를 위한 flag
        for i in range(len(f)):
            if f[i].isnumeric(): # NUMBER 부분 필터링
                num += f[i]
                flag = True
            elif not flag: # HEAD 부분 필터링
                head += f[i]
            else: # TAIL 부분 필터링
                tail += f[i:]
                break
        answer.append((head, num, tail))

    # HEAD, NUMBER 순서로 정렬
    # HEAD는 대소문자 구분하지 않고 정렬
    # NUMBER는 정수로 정렬 ex) 01, 14, 02, 24 -> 1, 2, 14, 24와 같이 크기 순으로 오름차순 정렬
    # 단, 정렬을 함에 있어 기존 값이 바뀌면 안되므로 sort 함수의 key 값에서 정렬 기준을 설정하여 값을 변환해서 정렬할 수 있게끔
    answer.sort(key=lambda x: (x[0].upper(), int(x[1])))

    return [''.join(answer[i]) for i in range(len(answer))]
