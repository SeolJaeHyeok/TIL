m, n = map(int, input().split())

# 숫자 -> 영어 변환 테이블
table = {
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine',
    '0': 'zero',
}

array = []
# 범위 안의 숫자들을 영어로 추가
for i in range(m, n + 1):
    num = str(i)
    tmp = []
    for char in num:
        tmp.append(table[char])
    array.append(tmp)

# 사전 순으로 정렬
array.sort()

# 영어 -> 숫자 변환 테이블
rtable = dict(map(reversed, table.items()))
answer = []
# 영어로 저장된 배열을 다시 숫자로 변환시켜주기
for s in array:
    tmp = ''
    for i in range(len(s)):
        tmp += rtable[s[i]]
    answer.append(int(tmp))

# 조건에 맞춰 출력
for i in range(len(answer)):
    if i != 0 and i % 10 == 0:
        print()
    print(answer[i], end=' ')


