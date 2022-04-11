import sys
input = sys.stdin.readline

while True:
    word = input().rstrip()
    # end 입력 받으면 탈출
    if word == 'end':
        break

    # 모음을 담은 리스트
    moeum = ['a', 'e', 'i', 'o', 'u']
    flag = False # 조건에 만족하는지 체크하는 변수, 초기값은 False

    # Case1
    # 모음이 존재하는지 검사
    for m in moeum:
        # 모음이 하나라도 있는 경우 True
        if m in word:
            flag = True
            break

    # Case2
    # 모음과 자음이 연속으로 3개 나오는지 검사
    mo_count, za_count = 0, 0
    for i in range(len(word)):
        if word[i] in moeum:
            mo_count += 1
            za_count = 0
        else:
            za_count += 1
            mo_count = 0

        # 자음 또는 모음이 연속으로 3개 나오는 경우 False
        if za_count == 3 or mo_count == 3:
            flag = False

    # Case3
    # 같은 글자가 연속으로 두 개 나오는지 검사
    for i in range(len(word) - 1):
        # ee, oo는 예외 처리
        if word[i] + word[i + 1] == 'ee' or word[i] + word[i + 1] == 'oo':
            continue
        # 그 외에 같은 문자가 두 개 연속으로 나오면 False
        if word[i] == word[i + 1]:
            flag = False
            break

    if flag:
        print(f'<{word}> is acceptable.')
    else:
        print(f'<{word}> is not acceptable.')