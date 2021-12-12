# 한윤정이 이탈리아에 가서 아이스크림을 사먹는데
# dfs 풀이에 비해 메모리를 많이 잡아 먹는다.
from itertools import combinations

n, m = map(int, input().split())
# 아이스크림 번호 초기화
ices = [i for i in range(1, n + 1)]
# 아이스크림 번호마다 안 좋은 조합을 추가할 2차원 리스트 초기화, 1번 아이스크림 -> 인덱스 1
table = [[] * i for i in range(n + 1)]

# 안 좋은 조합을 테이블에 추가
for _ in range(m):
    a, b = map(int, input().split())
    table[a].append(b)

# 가능한 모든 조합 추출
all_ice = list(combinations(ices, 3))
total = len(list(combinations(ices, 3)))

# 모든 조합을 순회하면서
for one, two, three in all_ice:
    # 해당 조합이 안 좋은 조합이라면 -1
    if two in table[one] or three in table[one] \
            or one in table[two] or three in table[two]\
            or one in table[three] or two in table[three]:
        total -= 1

print(total)