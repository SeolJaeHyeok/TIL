import sys
from collections import Counter
input = sys.stdin.readline

word = list(input().rstrip())
alpha = Counter(word)

odd_count = 0
flag = True
mid = ''
for al, cnt in alpha.items():
    if cnt % 2 != 0:
        odd_count += 1
        mid = al
        word.remove(al)

    if odd_count > 1:
        flag = False
        break

word.sort()

if not flag:
    print('I\'m Sorry Hansoo')
else:
    front = []
    for i in range(0, len(word), 2):
        front.append(word[i])

    front = ''.join(front)
    back = ''.join(reversed(front))
    print(front + mid + back)

"""
핵심 - 팰린드롬을 만들기 위해서는 홀수개 등장하는 알파벳이 2번 이상 나타나서는 안된다. -> 2번 이상 등장하면 팰린드롬 불가능
-> 홀수개 등장하는 알파벳을 하나 제거 후(다른 변수에 저장) 해당 알파벳의 등장 횟수를 0 또는 짝수개로 만든 다음 모든 알파벳이 짝수개가 되도록 만든다.
-> 남은 알파벳들을 하나씩 건너뛰며 저장하여 앞의 문자열을 만들고 이를 뒤집어 뒤의 문자열을 만든다
-> 제거한 다음 저장한 알파벳은 문자열의 가운데 위치한다.
"""