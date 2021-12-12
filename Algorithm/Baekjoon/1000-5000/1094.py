# 막대기
# 1
x = int(input())
count = 0

while x != 0:
    if x % 2 == 1:
        count += 1
    x //= 2

print(count)

# 2
x = int(input())
sticks = [64,32, 16, 8, 4, 2, 1]

count = 0
for stick in sticks:
    while x - stick >= 0:
        count += 1
        x -= stick

print(count)


