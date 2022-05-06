import sys
input = sys.stdin.readline

n, k = map(int, input().split())

count = 0

for hour in range(n + 1):
    if hour < 10:
        hour = '0' + str(hour)
    else:
        hour = str(hour)
    for minute in range(60):
        if minute < 10:
            minute = '0' + str(minute)
        else:
            minute = str(minute)
        for second in range(60):
            if second < 10:
                second = '0' + str(second)
            else:
                second = str(second)

            k = str(k)
            if k in hour or k in minute or k in second:
                count += 1

print(count)