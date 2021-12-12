n = int(input())
m, k = map(int, input().split())
pens = list(map(int, input().split()))

pens.sort(reverse=True)
total = m * k

count = 0
for pen in pens:
    count += 1
    total -= pen
    if total <= 0:
        break

if total <= 0:
    print(count)
else:
    print("STRESS")

