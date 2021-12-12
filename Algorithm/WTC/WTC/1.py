# 우테코 2기 1번
def solution(money):
    # 화폐 단위 초기화
    cash = [50000, 10000, 5000, 1000, 500, 100, 50, 10, 1]
    answer = []

    # 큰 화폐단위부터 계산
    for c in cash:
        # 화폐단위로 나눠주고
        a = money // c
        # 몫(각 화폐의 개수) 추가
        answer.append(a)
        # 각 화폐 단위로 나눈 나머지로 money 갱신
        money %= c

    return answer


print(solution(50237))
print(solution(15000))
