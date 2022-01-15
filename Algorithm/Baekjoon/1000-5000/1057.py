import sys
input = sys.stdin.readline

n, a, b = map(int, input().split())

count = 0
while a != b:
    a -= a//2
    b -= b//2
    count += 1

print(count)

"""
토너먼트는 2로 나눈 몫을 뺀 값이 같아졌을 때가 서로 대결하는 순간이 된다. 
따라서 두 값이 같아질 때까지 2로 나누고 라운드를 증가시켜준다. 
ex) 16 8 9 라고 할 때
8 -> 4 -> 2 -> 1 -> 1
9 -> 5 -> 3 -> 2 -> 1
"""