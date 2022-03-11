# 효율 x
def solution(p):
    answer = 0
    for i in range(len(p)):
        # 왼쪽 및 오른쪽 화살표 체크
        left_check = right_check = True
        if p[i] == '<':  # 왼쪽 화살표인 경우
            # 해당 시작점부터 앞으로 탐색
            for j in range(i, -1, -1):
                # 오른쪽 화살표를 만난경우 체크
                if p[j] == '>':
                    right_check = False
                    break
        else:  # 오른쪽 화살표인 경우
            # 해당 시작점부터 뒤로 탐색
            for j in range(i, len(p)):
                # 왼쪽 화살표를 만난 경우 체크
                if p[j] == '<':
                    left_check = False
                    break

        # 반대되는 화살표를 만난 적이 없을 경우 카운팅
        if left_check and right_check:
            answer += 1

    return answer
solution("<<<><")