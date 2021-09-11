# 위에서 아래로
# my
n = int(input())

result = []
for i in range(n):
    result.append(int(input()))

result.sort(reverse=True)
# result = sorted(result, reverse=True)

for i in result:
    print(i, end=' ')

