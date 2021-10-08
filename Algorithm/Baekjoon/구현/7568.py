# 7568
n = int(input())

array = []
for i in range(n):
    array.append(tuple(map(int, input().split())))

count = 1

for i in range(len(array)):
    tmp_x, tmp_y = array[i]
    count = 1
    for x, y in array:
        if tmp_x < x and tmp_y < y:
            count += 1
    print(count, end=' ')
