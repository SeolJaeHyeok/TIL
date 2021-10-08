# 1924
month, day = map(int, input().split())
table = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
day_table = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for i in range(month - 1):
    day += day_table[i]

print(table[day % 7])




