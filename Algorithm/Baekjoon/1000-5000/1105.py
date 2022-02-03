# 1, 시간 초과
import sys
input = sys.stdin.readline

l, r = map(int, input().split())
answer = 1e9
for i in range(l, r + 1):
    tmp = 0
    target = str(i)
    for t in target:
        if t == '8':
            tmp += 1
    answer = min(answer, tmp)

print(answer)

# Sol
import sys
input = sys.stdin.readline

l, r = map(int, input().split())

answer = 0
# 자릿수가 다른경우 답은 항상 0
if len(str(l)) != len(str(r)):
    print(0)
else: # 자릿수가 같은 경우
    l_str = str(l)
    r_str = str(r)
    # 첫째 자릿수가 다른 경우 답은 항상 0
    if l_str[0] != r_str[0]:
        print(0)
    else:
        # 자릿수가 같고 첫째 자리의 수가 8이라면 답은 1 이상
        if l_str[0] == '8':
            answer += 1

        for i in range(1, len(l_str)):
            if l_str[i] != r_str[i]:
                break
            else:
                if l_str[i] == '8':
                    answer += 1
        print(answer)

