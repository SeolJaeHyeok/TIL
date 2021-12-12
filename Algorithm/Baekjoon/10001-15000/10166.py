a, b = map(int, input().split())
result = set()

for i in range(a, b+1):
    for j in range(1, i+1):
        result.add(j/i)

print(len(result))
