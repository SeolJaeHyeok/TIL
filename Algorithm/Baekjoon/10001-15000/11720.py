import sys
input = sys.stdin.readline

n = int(input())
word = input().rstrip()

answer = 0
for char in word:
    answer += int(char)

print(answer)
