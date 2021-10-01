# 문자열 재정렬
word = input()

sum = 0
alpha = []
for w in word:
    s = ord(w) - 48
    if int(s) < 10:
       sum += int(s)
    else:
        alpha.append(chr(s+48))

alpha.sort()
alpha.append(str(sum))

print(''.join(alpha))


# sol
data = input()
result = []
value = 0

# 문자를 하나씩 확인하며
for x in data:
    # 알파벳인 경우 결과 리스트에 삽입
    if x.isalpha():
        result.append(x)
    # 숫자는 따로 더하기
    else:
        value += int(x)

# 알파벳을 오름차순으로 정렬
result.sort()

# 숫자가 하나라도 존재하는 경우 가장 뒤에 삽입
if value != 0:
    result.append(str(value))

# 최종 결과 출력(리스트를 문자열로 변환하여 출력)
print(''.join(result))


"""
접근 방법
- 알파벳 대문자와 숫자(0~9)가 입력된다는 조건이 있으므로 ord()함수를 이용해 숫자와 알파벳을 분리하여 처리
- 풀이에서는 isalpha() 함수를 이용해서 알파벳인 경우와 숫자인 경우를 분리하여 처리   
"""