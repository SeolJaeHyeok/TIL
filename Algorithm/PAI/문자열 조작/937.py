# Reorder Log Files
# 람다와 + 연산자를 이용,
def reorderLogFiles(logs: list):
    digits = [] # 숫자 로그를 담을 배열
    letters = [] # 문자 로그를 담을 배열
    # 로그 배열을 순회
    for log in logs:
        # 숫자 로그로 이루어진 경우, isdigit 메서드로 검사
        if log.split()[1].isdigit():
            digits.append(log)
        else:
            letters.append(log)

    # 문자로 구성된 로그 정렬, 문자를 기준으로 정렬하고 그런 다음 식별자를 기준으로 정렬
    letters.sort(key=lambda x: (x.split()[1], x[0]))
    # 문자로 구성된 로그가 숫자로 구성된 로그 앞에 오게끔 리턴
    return letters + digits 


logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
result = reorderLogFiles(logs)
print(result)
