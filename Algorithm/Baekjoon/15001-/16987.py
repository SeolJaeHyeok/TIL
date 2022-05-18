import sys
input = sys.stdin.readline

n = int(input())
eggs = []
for _ in range(n):
    a, b = map(int, input().split())
    eggs.append([a, b])

answer = 0
def process(nowIdx):
    global answer
    # 종료 조건
    # 현재 들고 있는 계란이 가장 오른쪽에 위치한 계란일 경우
    if nowIdx == n:
        tmp = 0 # 깨진 계란의 갯수
        for i in range(n):
            # 현재 들고 있는 계란이면 무시
            if eggs[i][0] == nowIdx:
                continue
            # 다른 계란 중 내구도가 0이하로 내려간 계란 카운팅
            if eggs[i][0] <= 0:
                tmp += 1
        # 정답 갱신
        answer = max(answer, tmp)
        return

    # 손에 든 계란이 깨진 경우 다음 계란 선택
    if eggs[nowIdx][0] <= 0:
        process(nowIdx + 1)
        return

    # 자신을 제외한 모든 계란이 깨져있으면 정답 갱신
    flag = True
    for i in range(n):
        if nowIdx == i:
            continue
        # 깨지지 않은 계란이 하나라도 있을 시 탈출
        if eggs[i][0] > 0:
            flag = False
            break
    # 모두 깨졌다면 정답 갱신 후 끝내기
    if flag:
        answer = max(answer, n - 1)
        return

    # 자신을 제외한 계란 부딪히기
    for targetIdx in range(n):
        # 자신인 경우 무시
        if nowIdx == targetIdx:
            continue
        # 이미 깨진 계란도 무시
        if eggs[targetIdx][0] <= 0:
            continue

        # 다른 계란인 경우 각 계란의 내구도를 상대 계란의 무게만큼 감소시키기
        eggs[nowIdx][0] -= eggs[targetIdx][1]
        eggs[targetIdx][0] -= eggs[nowIdx][1]
        # 부딪히고 다음 계란 선택
        process(nowIdx + 1)
        # 퇴각할 때 원래대로 복구
        eggs[nowIdx][0] += eggs[targetIdx][1]
        eggs[targetIdx][0] += eggs[nowIdx][1]


process(0)
print(answer)