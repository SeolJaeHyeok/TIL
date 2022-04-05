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