def solution(N, stages):
    answer = []
    users = len(stages)  # 전체 유저 수
    for i in range(1, N + 1):
        # 해당 스테이지에 머무르고 있는 유저
        count = stages.count(i)
        for stage in stages:
            if users == 0:  # 스테이지에 도달한 유저가 없으면
                fail = 0  # 실패율 0
            else:  # 스테이지에 도달한 유저가 있으면
                fail = count / users  # 실패율 계산

        answer.append((i, fail))  # 현재 스테이지와 실패율 추가
        users -= count  # 유저 수 갱신

    answer.sort(key=lambda x: x[1], reverse=True)

    result = [answer[i][0] for i in range(len(answer))]

    return result