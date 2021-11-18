# 2018 카카오 블라인드 3차 압축
from collections import defaultdict


def solution(msg):
    answer = []
    table = defaultdict(int)
    for i in range(26):
        table[chr(65 + i)] = i + 1

    start = end = 0
    while True:
        # 글자 길이를 1씩 늘려가며 검사
        end += 1
        # 마지막 인덱스 값이 마지막 글자라면 끝까지 추가하고 종료
        if end == len(msg):
            answer.append(table[msg[start:end]])
            break

        # 한 글자씩 늘려가며 테이블에 존재하는지 검사
        # 없다면 테이블의 길이 + 1을 값으로 하여 저장하고
        # 이전까지 구한 글자의 색인을 테이블에서 찾아 추가하고 시작점 변경
        if msg[start:end + 1] not in table:
            answer.append(table[msg[start:end]])
            table[msg[start:end + 1]] = len(table) + 1
            start = end

    return answer
