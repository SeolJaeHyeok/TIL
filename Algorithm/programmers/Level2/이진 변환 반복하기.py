def solution(s):
    count, zero_count = 0, 0

    while s != '1':
        zero_count += s.count('0')
        s = s.replace('0', '')
        s = bin(len(s))[2:]
        count += 1

    return [count, zero_count]

print(solution("110010101001")) # [3,8]
print(solution("01110")) # [3,3]
print(solution("1111111")) # [4,1]