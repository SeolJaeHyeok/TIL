import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    word = ''.join(input().split(' ')).rstrip()
    table = [0] * 26

    for char in word:
        table[ord(char) - 97] += 1

    if table.count(max(table)) > 1:
        print('?')
    else:
        print(chr(97 + table.index(max(table))))