# Section05-3
# 파이썬 흐름제어(제어문)
# 제어문 관련 퀴즈(정답은 영상)

# 1 ~ 5 문제 if 구문 사용
# 1. 아래 딕셔너리에서 '가을'에 해당하는 과일을 출력하세요.
q1 = {"봄": "딸기", "여름": "토마토", "가을": "사과"}
for key in q1:
    if key == '가을':
        print(q1[key])

for k, v in q1.items():
    if k == '가을':
        print(v)
# 2. 아래 딕셔너리에서 '사과'가 포함되었는지 확인하세요.
q2 = {"봄": "딸기", "여름": "토마토", "가을": "사과"}
for value in q2.values():
    if value == '사과':
        print('사과가 포함되어 있음')
        break
else:
    print('사과가 포함되어 있지 않음')

# 3. 다음 점수 구간에 맞게 학점을 출력하세요.
# 81 ~ 100 : A학점
# 61 ~ 80 :  B학점
# 41 ~ 60 :  C학점
# 21 ~ 40 :  D학점
#  0 ~ 20 :  E학점

score = 0
if score > 80:
    print('A')
elif score > 60:
    print('B')
elif score > 40:
    print('C')
elif score > 20:
    print('D')
else:
    print('E')


# 4. 다음 세 개의 숫자 중 가장 큰수를 출력하세요.(if문 사용) : 12, 6, 18

a, b, c = 12, 6, 18
maxNum = a

if b > a:
    maxNum = b
if c > b:
    maxNum = c
print(maxNum)
print(max(a, b, c))
# 5. 다음 주민등록 번호에서 7자리 숫자를 사용해서 남자, 여자를 판별하세요. (1,3 : 남자, 2,4 : 여자)
num = '940806-1168021'

if int(num[7]) % 2 != 0:
    print('남자')
else:
    print('여자')
# 6 ~ 10 반복문 사용(while 또는 for)

# 6. 다음 리스트 중에서 '정' 글자를 제외하고 출력하세요.
q3 = ["갑", "을", "병", "정"]

for s in q3:
    if s == '정':
        continue
    print(s, end=' ')

print()
# 7. 1부터 100까지 자연수 중 '홀수'만 한 라인으로 출력 하세요.
for i in range(1,101,2):
    print(i, end=" ")

print()
# 8. 아래 리스트 항목 중에서 5글자 이상의 단어만 출력하세요.
q4 = ["nice", "study", "python", "anaconda", "!"]

for v in q4:
    if len(v) >= 5:
        print(v)
    else:
        continue
# 9. 아래 리스트 항목 중에서 소문자만 출력하세요.
q5 = ["A", "b", "c", "D", "e", "F", "G", "h"]

for a in q5:
    if a.islower():
        print(a)
    else:
        continue

# 10. 아래 리스트 항목 중에서 소문자는 대문자로 대문자는 소문자로 출력하세요.
q6 = ["A", "b", "c", "D", "e", "F", "G", "h"]
for a in q6:
    if a.islower():
        print(a.upper())
    else:
        print(a.lower())