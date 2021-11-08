# 암호
# 암호화된 문자열 복구하기
k = int(input())
data = input()
length = len(data) // k

array = []
for i in range(0, len(data), k):
    tmp = []
    for j in range(i, i + k):
        tmp.append(data[j])
    array.append(tmp)

for i in range(len(array)):
    if i % 2 != 0:
        array[i].reverse()

answer = ''
for i in range(len(array[0])):
    for j in range(len(array)):
        answer += array[j][i]

print(answer)


# 문자열 암호화
k = int(input())
data = input()
length = len(data) // k

answer = ''
array = [[] for _ in range(length)]
for i in range(len(data)):
    array[i % length].append(data[i])

for i in range(len(array)):
    if i % 2 == 0:
        for j in range(len(array[0])):
            answer += array[i][j]
    else:
        for j in range(len(array[0])-1, -1, -1):
            answer += array[i][j]

print(answer)
