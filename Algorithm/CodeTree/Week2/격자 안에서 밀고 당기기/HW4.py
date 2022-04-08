"""
길이가 n인 문자열 A가 주어졌을 때, 적절하게 특정 횟수만큼 오른쪽으로 shift하여,
shift 된 이후의 문자열에 Run-Length Encoding을 진행했을 때의 길이가 최소가 되도록 하려고 합니다.

Run-Length Encoding이란 간단한 비손실 압축 방식으로, 연속해서 나온 문자와 연속해서 나온 개수로 나타내는 방식입니다.
예를 들어, 문자열 A가 aaabbbbcaa인 경우 순서대로 a가 3번, b가 4번, c가 1번 그리고 a가 2번 나왔으므로
Run-Length Encoding을 적용하게 되면 a3b4c1a2이 되며 길이는 8이 됩니다.

만약 문자열 A에 해당하는 aaabbbbcaa를 오른쪽으로 2번 shift를 하게 되면 aaaaabbbbc가 되며,
이에 Run-Length Encoding을 적용하게 되면 a5b4c1이 되므로 길이가 6이 되어 최소가 됩니다.
shift를 진행하여 나올 수 있는 Run-Length Encoding 이후의 결과들 중 최소 길이를 구하는 프로그램을 작성해보세요.

aaabbbbcaa
6

aaaaaaaaaa
3
"""
import sys
from collections import deque
input = sys.stdin.readline

def run_length_encoding(str_list):
    encoding = ""
    seq = 1
    tmp_char = str_list[0]
    for idx in range(len(str_list) - 1):
        if str_list[idx] == str_list[idx+1]:
            seq += 1
        else:
            encoding += tmp_char + str(seq)
            seq = 1
            tmp_char = str_list[idx+1]

    encoding += tmp_char + str(seq)
    return len(encoding)

word = deque(input())

answer = 1e9
for _ in range(len(word)):
    word.rotate()
    # print(word)
    answer = min(answer, run_length_encoding(word))

print(answer)