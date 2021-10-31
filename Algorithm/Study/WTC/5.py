# 우테코 2기 5번
def solution(num):
    count = 0
    for i in range(1, num + 1):
        n = str(i)
        count += n.count('3')
        count += n.count('6')
        count += n.count('9')

    return count

print(solution(13))
print(solution(33))
print(solution(23))
print(solution(39))

