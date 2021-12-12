def process(n, m):
    count = 0
    for i in range(n, m + 1):
        s = str(i)
        flag = True
        for j in range(len(s)):
            for k in range(j + 1, len(s)):
                if s[j] == s[k]:
                    flag = False
                    break
        if flag:
            count += 1

    return count


while True:
    try:
        n, m = map(int, input().split())
        print(process(n, m))
    except:
        break