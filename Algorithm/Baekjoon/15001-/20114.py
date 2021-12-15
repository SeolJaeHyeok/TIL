n, h, w = map(int, input().split())
words = [input() for _ in range(h)]
answer = ["?" for _ in range(n)]
# print(words)
# print(answer)

for word in words:
    idx = 0
    for i in range(n):
        for char in word[idx:idx+w]:
            if char != "?":
                answer[i] = char
        idx += w

print("".join(answer))
