import sys
input = sys.stdin.readline

word = input().rstrip()
table = ['U', 'C', 'P', 'C']

flag = True
for t in table:
    if t in word:
        word = word[word.index(t) + 1: ]
    else:
        flag = False
        break

if flag:
    print('I love UCPC')
else:
    print('I hate UCPC')