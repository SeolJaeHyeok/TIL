def solution(s, n):
    answer = []
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():
            answer.append(chr(65 + (ord(s[i]) - 65 + n) % 26))
        elif s[i].islower():
            answer.append(chr(97 + (ord(s[i]) - 97 + n) % 26))
        else:
            answer.append(s[i])
    return ''.join(answer)