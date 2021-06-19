# # 1330번
# A, B = map(int, input().split())
# if A > B:
#     print('>')
# elif A < B:
#     print('<')
# else:
#     print('==')

# 9498번
# score = int(input())
# if score >= 90:
#     print('A')
# elif score >= 80:
#     print('B')
# elif score >= 70:
#     print('C')
# elif score >= 60:
#     print('D')
# else:
#     print('F')

# 2753번
# year = int(input())
#
# if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
#     print('1')
# else:
#     print('0')

# 14681번
# x = int(input())
# y = int(input())
#
# if x > 0 and y > 0:
#     print('1')
# elif x < 0 and y > 0:
#     print('2')
# elif x < 0 and y < 0:
#     print('3')
# else:
#     print('4')

# 2884번
# My Solution
H, M = map(int, input().split())

if H == 0:
    H = 23
    if M < 45:
        M += 15
    else:
        M -= 45
else:
    if M < 45:
        H -= 1
        M += 15
    else:
        M -= 45

print(H, M)

# Other Solution
H, M = map(int, input().split())

if M < 45:  # 분단위가 45분보다 작을 때
    if H == 0:  # 0 시이면
        H = 23
        M += 60
    else:  # 0시가 아니면 (0시보다 크면)
        H -= 1
        M += 60

print(H, M - 45)
