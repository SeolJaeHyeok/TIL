# 11721
data = list(input())

count = 0
for i in range(len(data)):
    print(data[i], end='')
    count += 1
    if count >= 10:
        count = 0
        print()
