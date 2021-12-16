# 1, 2506ms
import sys
from collections import defaultdict

Q = int(input())

answer = 0
price_table = defaultdict(list)
for _ in range(Q):
    array = list(sys.stdin.readline().split())
    c, name, k = int(array[0]), array[1], int(array[2])
    if c == 1:
        prices = [int(i) for i in array[3:]]
        for i in prices:
            price_table[name].append(i)
            price_table[name].sort(reverse=True)
    else:
        for p in price_table[name][:k]:
            answer += p
            price_table[name].remove(p)

print(answer)

# 2, 504ms
import sys
from collections import defaultdict

Q = int(input())

answer = 0
price_table = defaultdict(list)
for _ in range(Q):
    array = list(sys.stdin.readline().split())
    name = array[1]
    if array[0] == '1':
        price_table[name].extend(list(map(int, array[3:])))
    else:
        k = int(array[2])
        if k > len(price_table[name]):
            answer += sum(price_table[name])
            price_table[name].clear()
        else:
            price_table[name].sort()
            answer += sum(price_table[name][-k:])
            for _ in range(k):
                price_table[name].pop()

print(answer)


# 다른 사람 풀이 heapq 이용
import sys, heapq
input = sys.stdin.readline

info = dict()
Q = int(input())
answer = 0
for q in range(Q):
    lst = list(input().rstrip('\n').split())
    if lst[0] == '1':
        id , cnt = lst[1], int(lst[2])
        if id not in info.keys():
            info[id] = []
        for i in range(cnt):
            heapq.heappush(info[id], -1*int(lst[3+i]))
    else:
        id , cnt = lst[1], int(lst[2])
        if id not in info.keys(): continue
        for i in range(min(cnt, len(info[id]))):
            answer -= heapq.heappop(info[id])
print(answer)