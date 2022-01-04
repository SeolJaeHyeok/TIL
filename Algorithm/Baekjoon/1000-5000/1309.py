import sys
input = sys.stdin.readline

n = int(input())

left, right, nothing = [0] * (n + 1), [0] * (n + 1), [0] * (n + 1)

nothing[0] = 1
for i in range(1, n+1):
    nothing[i] = (left[i-1] + right[i-1] + nothing[i-1]) % 9901
    left[i] = (right[i-1] + nothing[i-1]) % 9901
    right[i] = (left[i-1] + nothing[i-1]) % 9901

print((nothing[n]+left[n]+right[n]) % 9901)
