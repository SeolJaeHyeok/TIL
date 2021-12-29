from itertools import combinations

array = sorted([int(input()) for _ in range(9)])

c = list(combinations(array, 7))
for i in range(len(c)):
    if sum(c[i]) == 100:
        for a in c[i]:
            print(a)
        break
