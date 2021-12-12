# 보물
# 1
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

result = 0
while len(a) != 0:
    max_value = max(a)
    min_value = min(b)
    result += max_value * min_value
    a.remove(max_value)
    b.remove(min_value)

print(result)

# 2
n = int(input())
a = sorted(list(map(int, input().split())))
b = sorted(list(map(int, input().split())), reverse=True)

result = 0
for i in range(len(a)):
    result += a[i] * b[i]

print(result)