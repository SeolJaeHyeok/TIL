# ROT13
# 1, 일일이 범위 지정
def caesarCipher(s):
    answer = ''
    for char in s:
        alphaNum = ord(char)
        # 문자가 알파벳인 경우
        if char.isalpha():
            # 13자리 옮겼을 때 알파벳 소문자 범위를 벗어나는 경우
            if 78 <= alphaNum <= 90:
                answer += chr(alphaNum - 13)
            # 13자리 옮겼을 때 알파벳 대문자 범위를 벗어나는 경우
            elif 110 <= ord(char) <= 122:
                answer += chr(alphaNum - 13)
            else:
                answer += chr(alphaNum + 13)
        # 알파벳이 아니라면 그대로 추가
        else:
            answer += char

    return answer


input_data = input()
result = caesarCipher(input_data)
print(result)


# 나머지 연산 이용
def caesarCipher(s):
    answer = ''
    for char in s:
        if char.isalpha():
            # 대문자인 경우
            if char.isupper():
                answer += chr(65 + (ord(char) + 13 - 65) % 26)
            # 소문자인 경우
            else:
                answer += chr(97 + (ord(char) + 13 - 97) % 26)
        # 알파벳이 아닌 경우
        else:
            answer += char

    return answer


input_data = input()
result = caesarCipher(input_data)
print(result)