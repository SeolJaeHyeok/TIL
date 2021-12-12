# 10162
# 1
t = int(input())
array = [300, 60, 10]
table = [0, 0, 0]

for i in range(len(array)):
    count = 0
    count += t // array[i]
    t %= array[i]
    table[i] = count

if t:
    print(-1)
else:
    for i in table:
        print(i, end=' ')

# 2
t = int(input())

if t % 10 != 0:
    print(-1)
else:
    A = B = C = 0
    A = t // 300
    B = (t % 300) // 60
    C = ((t % 300) % 60) // 10
    print(A, B, C)

