import sys
import copy
input = sys.stdin.readline

s = list(input().rstrip())
t = list(input().rstrip())

s_len = len(s)
t_len = len(t)

# 두 값의 길이의 최소공배수
lcm = 0
for i in range(max(s_len, t_len), s_len * t_len + 1):
    if i % s_len == 0 and i % t_len == 0:
        lcm = i
        break

# s의 길이를 최소공배수만큼 반복
for i in range(s_len, lcm):
    s.append(s[i % s_len])

# t의 길이를 최소공배수만큼 반복
for i in range(t_len, lcm):
    t.append(t[i % t_len])

if ''.join(s) == ''.join(t):
    print(1)
else:
    print(0)