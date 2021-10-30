# 암호 만들기
from itertools import combinations
import sys

l, c = map(int, sys.stdin.readline().split())
array = list(sys.stdin.readline().split())
array.sort()
comb = list(combinations(array, l))
a_table = ['a', 'e', 'i', 'o', 'u']
b_table = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']

for password in comb:
    a_count = b_count = 0
    for a in password:
        if a in a_table:
            a_count += 1
        if a in b_table:
            b_count += 1

    if 1 <= a_count and 2 <= b_count:
        print(''.join(password))
