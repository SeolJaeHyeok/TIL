# 친구
# 플로이드 워셜 알고리즘 이용
n = int(input())
array = []
for i in range(n):
    array.append(list(map(str, input())))

table = [[0 for _ in range(n)] for _ in range(n)]

for i in range(len(array)):
    for j in range(len(array)):
        for k in range(len(array)):
            if j == k:
                continue
            # j와 k가 서로 친구이거나 j가 i와 친구이고 k가 i와 친구일 경우
            if array[j][k] == 'Y' or (array[j][i] == 'Y' and array[k][i] == 'Y'):
                table[j][k] = 1 # j와 k는 2-친구

max_value = 0
for row in table:
    max_value = max(max_value, sum(row))

print(max_value)
