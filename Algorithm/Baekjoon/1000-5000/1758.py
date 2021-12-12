n = int(input())

array = []
for i in range(1, n+1):
    array.append(int(input()))

array.sort(reverse=True)

total = 0
for i in range(len(array)):
    tmp = array[i] - ((i+1) - 1)
    if tmp >= 0:
        total += tmp

print(total)