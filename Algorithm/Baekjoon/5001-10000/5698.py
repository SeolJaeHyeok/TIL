# Tautogram

while True:
    s = input().lower()
    if s == '*':
        break

    array = s.split()
    flag = True
    for i in range(1, len(array)):
        if array[i][0] != array[i-1][0]:
            flag = False
            break
    if flag:
        print('Y')
    else:
        print('N')
