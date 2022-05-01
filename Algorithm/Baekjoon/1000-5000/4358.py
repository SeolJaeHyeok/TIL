import sys
from collections import defaultdict
input = sys.stdin.readline

table = defaultdict(int)

while True:
    tree = input().rstrip()
    if not tree:
        break
    table[tree] += 1

total = sum(table.values())

tree_arr = list(table.keys())
tree_arr.sort()
for tree in tree_arr:
    print('%s %.4f' % (tree, table[tree] / total * 100))