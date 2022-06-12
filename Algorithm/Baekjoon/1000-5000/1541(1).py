import sys
input = sys.stdin.readline

op = input().rstrip().split("-")
answer = 0

# 첫 -가 나오기전까지는 모두 더하기
for i in op[0].split('+'):
    answer += int(i)

# 그 다음 요소부터는 모두 뺴주기
for o in op[1:]:
    # -로 구분한 결과가 ['90', '60', '30+60']와 같이 나올 수 있으므로
    # +로 다시 split 해줘야한다.
    for i in o.split('+'):
        answer -= int(i)

print(answer)