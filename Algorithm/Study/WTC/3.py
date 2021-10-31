# 우테코 2기 3번
def solution(c):
    answer = ''
    for char in c:
        # 알파벳인 경우 치환
        if char.isalpha():
            # 대문자(65~90)인 경우
            if char.isupper():
                tmp = ord(char) - 65
                answer += chr(90 - tmp)
            # 소문자(97~122)인 경우
            else:
                tmp1 = ord(char) - 97
                answer += chr(122 - tmp1)
        # 알파벳이 아니면 그냥 더해주기
        else:
            answer += char
    return answer

print(solution('I love you'))

