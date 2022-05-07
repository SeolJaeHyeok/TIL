import sys
input = sys.stdin.readline

words = []
length = []
for _ in range(5):
    word = input().rstrip()
    words.append(word)
    length.append(len(word))

answer = ''
for i in range(max(length)):
    for j in range(5):
        if i < length[j]:
            answer += words[j][i]

print(answer)