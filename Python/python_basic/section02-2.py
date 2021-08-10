# Section02-2
# 몸풀기

# import this
import sys

# Python 기본 인코딩
print(sys.stdin.encoding)
print(sys.stdout.encoding)

# 출력
print('I\'m a goodboy')

# 변수
myName = 'Goodboy'
print(f'I\'m a {myName}')

if myName == 'Goodboy':
    print('Ok')

print()

# 반복문
for i in range(1, 10):
    for j in range(1, 10):
        print('%d * %d = %d' % (i, j, i*j))

print()

# 함수


def sayHello(name):
    print(f'My name is {name}')


sayHello('JaeHyeok')

print()

# 클래스


class Cookie:
    pass


# 인스턴스 생성
cookie = Cookie()
print(type(cookie))
