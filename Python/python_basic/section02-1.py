# Section02-1
# 파이썬 기초
# Print

# 기본 출력
print('Hello Python!')
print("Hello Python!")
print("""Hello Python!""")
print('''Hello Python!''')

print()

# Seperator
print("Hello", "Python!", sep=",")
print("Hello", "Python!", sep="\n")
print("Hello", "Python!", sep="!")
print('2021', '08', '10', sep="-")

print()

# End
print('Welcome to the', end=" ")
print("Programming world.", end=" ")
print("Enjoy!")
print("test")

print()

# format
print('{} and {}'.format('You', 'Me'))
print('{a} and {b}'.format(a="You", b="Me"))
print('{0} and {1} and {0}'.format('You', 'Me'))
print("%s's favorite number is %d" % ("jaehyeok", 3))

name = 'jaehyeok'
number = 7
print(f"{name}'s favorite number is {number}")

print()

print("Test1:%5d, Price: %4.2f" % (776, 6543.123))
print("Test1:{0:5d}, Price: {1:4.2f}".format(776, 6543.123))
print("Test1:{a:5d}, Price: {b:4.2f}".format(a=776, b=6543.123))

print()

# escape code

"""
참고 : Escape 코드

\n : 개행
\t : 탭
\\ : 문자
\' : 문자
\" : 문자
\r : 캐리지 리턴
\f : 폼 피드
\a : 벨 소리
\b : 백 스페이스
\000 : 널 문자
...
"""
