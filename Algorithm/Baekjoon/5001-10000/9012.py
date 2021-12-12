# 9012번
def check(p):
    count = 0
    if p[0] == ')':
        print('NO')
        return

    for i in p:
        if i == '(':
            count += 1
        else:
            count -= 1
        if count < 0:
            print('NO')
            break

    if count == 0:
        print('YES')
    elif count > 0:
        print('NO')


n = int(input())

array = []
for i in range(n):
    array.append(input())

for data in array:
    check(data)

"""
접근 방법
- 입력된 문자열의 괄호의 개수를 세서 VPS인지 check
- 첫 문자가 ')'라면 VPS가 성립될 수 없으므로 NO 출력
- 그렇지 않다면 문자열을 순회하여 각 괄호의 개수를 세어서 알맞은 결과 출력
"""