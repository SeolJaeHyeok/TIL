from itertools import combinations

n, m = map(int, input().split())

array = []
for i in range(n):
    array.append(list(map(int, input().split())))

home = []
chicken = []
for i in range(n):
    for j in range(n):
        if array[i][j] == 1:
            home.append((i, j))
        elif array[i][j] == 2:
            chicken.append((i, j))


# 최대 M개의 치킨집을 고를 수 있다고 문제에 명시되어 있다.
# 선택된 치킨집이 많으면 많을수록 거리가 최소가 될 가능성이 크다.
# 즉, 전체 치킨집 중에서 m개를 선택하되, 그 중에서 거리가 가장 최소가 되는 곳으로 골라야 한다.
answer = 1e9
allChicken = list(combinations(chicken, m))
for c in allChicken:
    tmp = 0
    for h in home:
        # 각 집에서의 치킨거리 최소 값 더하기
        tmp += min([abs(h[0] - i[0]) + abs(h[1] - i[1]) for i in c])
        if answer <= tmp:
            break

    if tmp < answer:
        answer = tmp

print(answer)

