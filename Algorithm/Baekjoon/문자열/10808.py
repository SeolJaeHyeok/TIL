# 10808
s = input()
result = [0] * 26

for i in s:
    index = ord(i) - 97
    result[index] += 1

for i in result:
    print(i, end=' ')