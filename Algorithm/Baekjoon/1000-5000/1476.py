# 1476
e, s, m = map(int, input().split())
tmp_e = tmp_s = tmp_m = count = 1

while True:
    if e == tmp_e and s == tmp_s and m == tmp_m:
        break

    tmp_e += 1
    tmp_s += 1
    tmp_m += 1
    count += 1

    if tmp_e > 15:
        tmp_e = 1
    if tmp_s > 28:
        tmp_s = 1
    if tmp_m > 19:
        tmp_m = 1

print(count)
