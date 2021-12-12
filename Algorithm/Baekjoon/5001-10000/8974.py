a, b = map(int, input().split())
array = []

for i in range(1000):
    array += [i] * i

print(sum(array[a - 1:b]))