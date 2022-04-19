# 1
# import sys
# input = sys.stdin.readline
#
# n, m = map(int, input().split())
# a = list(map(int, input().split()))
# b = list(map(int, input().split()))
# a.extend(b)
# a.sort()
# print(*a)

# 2, Two pointer
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Two Pointer 변수 선언
a_start, b_start = 0, 0
a_end, b_end = len(a), len(b)

answer = []
while a_start != a_end or b_start != b_end:
    if a_start == a_end:
        answer.append(b[b_start])
        b_start += 1
    elif b_start == b_end:
        answer.append(a[a_start])
        a_start += 1
    else:
        if a[a_start] > b[b_start]:
            answer.append(b[b_start])
            b_start += 1
        else:
            answer.append(a[a_start])
            a_start += 1

print(*answer)