import sys
from collections import defaultdict

input = sys.stdin.readline
n = int(input())

table = defaultdict(int)  # 단축키로 지정된 알파벳 테이블

# 반복문을 통해 모든 단어를 확인
for _ in range(n):
    word = list(map(str, input().split()))

    # 1번과 2번
    for i in range(len(word)):
        # 현재 단어의 첫 글자가 단축기로 지정되어 있지 않다면
        if not table[word[i][0].upper()]:
            table[word[i][0].upper()] += 1  # 현재 단어의 첫 글자를 단축기로 지정
            word[i] = "[" + word[i][0] + "]" + word[i][1:]  # 현재 단어의 첫 글자를 "[]"를 감싼 후 출력.
            print(" ".join(word))
            break
    else:
        # 3번
        for j in range(len(word)):
            flag = False  # 현재 알파벳을 단축기로 사용했는지 유무
            for k in range(len(word[j])):
                # 현대 단어의 알파벳이 단축기로 지정되어 있지 않다면
                if not table[word[j][k].upper()]:
                    table[word[j][k].upper()] += 1  # 현재 단어의 첫 글자를 단축기로 지정
                    flag = True
                    word[j] = word[j][:k] + "[" + word[j][k] + "]" + word[j][k + 1:]  # 현재 단어의 첫 글자를 "[]"를 감싼 후 출력.
                    print(" ".join(word))
                    break
            if flag:
                break

        # 어떠한 알파벳으로도 단축기를 지정할 수 없는 경우
        else:
            print(*word)