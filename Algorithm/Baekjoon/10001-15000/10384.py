# 팬그램
n = int(input())
for i in range(n):
    s = input()
    s = s.lower()
    table = {}
    for j in range(ord('a'), ord('z') + 1):
        table[j] = 0

    for c in s:
        if ord('a') <= ord(c) <= ord('z'):
            table[ord(c)] += 1

    least = min(table.values())

    print("Case {}:".format(i + 1), end=" ")
    if least == 0:
        print("Not a pangram")
    elif least == 1:
        print("Pangram!")
    elif least == 2:
        print("Double pangram!!")
    else:
        print("Triple pangram!!!")

