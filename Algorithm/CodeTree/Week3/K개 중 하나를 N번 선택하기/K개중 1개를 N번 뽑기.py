import sys
input = sys.stdin.readline

k, n = map(int, input().split())
answer = []

def Choose():
    # n개의 원소를 뽑아냈으면 출력하고 함수 종료
    if len(answer) == n:
        print(*answer)
        return
    # 1 ~ k까지 재귀호출
    for i in range(1, k + 1):
        # 진입
        answer.append(i)
        Choose()
        # 퇴각할 때 진입 직전의 숫자를 빼줘야 다음 숫자에게 공정한 기회를 줄 수 있음
        answer.pop()

    return

Choose()