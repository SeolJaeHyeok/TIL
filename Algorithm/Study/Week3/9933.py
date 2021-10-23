# 민균이의 비밀번호
def solution(files):
    for i in range(len(files)):
        password = list(files[i])
        for j in range(len(files)):
            revPassword = list(reversed(files[j]))
            if password == revPassword:
                return password


n = int(input())
array = []
for i in range(n):
    array.append(input())

result = solution(array)
print(len(result), result[len(result) // 2])



