# 11654번
"""
알파벳 소문자, 대문자, 숫자 0-9중 하나가 주어졌을 때, 주어진 글자의 아스키 코드값을 출력하는 프로그램
"""
value = input()
print(ord(value))

# 11720번
"""
N개의 숫자가 공백 없이 쓰여있다. 이 숫자를 모두 합해서 출력하는 프로그램을 작성하시오.
"""
N = int(input())
num = input()
sumOfNum = 0
if len(num) == N:
    for i in num:
        sumOfNum += int(i)
else:
    print('Error Occurred')
    pass

print(sumOfNum)

# 10809번
"""
문제 
알파벳 소문자로만 이루어진 단어 S가 주어진다. 
각각의 알파벳에 대해서, 단어에 포함되어 있는 경우에는 처음 등장하는 위치를, 포함되어 있지 않은 경우에는 -1을 출력하는 프로그램을 작성하시오.

출력
각각의 알파벳에 대해서, a가 처음 등장하는 위치, b가 처음 등장하는 위치, ... z가 처음 등장하는 위치를 공백으로 구분해서 출력한다.
만약, 어떤 알파벳이 단어에 포함되어 있지 않다면 -1을 출력한다. 단어의 첫 번째 글자는 0번째 위치이고, 두 번째 글자는 1번째 위치이다.
=> find 함수를 이용해서 원하는 출력과 똑같은 결과를 도출할 수 있음. 
=> find와 비슷한 index 함수가 있지만 index 함수는 해당하는 문자열이 없으면 -1 반환하는 대신 Attribute Error 발생시킴 
"""
value = input()  # 입력
lowerCase = value.lower()  # 소문자로 변환
initialTable = list(range(97, 123))  # 알파벳 소문자 아스키 코드 97~122의 리스트 생성

for alpha in initialTable:
    print(lowerCase.find(chr(alpha)))  # 각각의 아스키코드에 해당하는 숫자를 chr함수를 이용해 문자열로 바꾼 뒤 그 문자를 입력한 단어 안에서 찾고 해당하는 위치 반환
