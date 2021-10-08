# 1316
def group_checker(s):
    for i in range(len(s) - 1):
        # 어느 한 글자가 다음 글자와 같지 않을 경우
        if s[i] != s[i + 1]:
            # 해당 글자가 다음 글자부터 단어 끝까지 존재하는지 확인하여 있다면 그룹 단어가 아니므로 False
            if s[i] in s[i + 1:]:
                return False
    return True


n = int(input())

array = []
for i in range(n):
    array.append(input())

for s in array:
    if not group_checker(s):
        n -= 1

print(n)

"""
- 최대 갯수의 그룹 단어는 입력된 n개의 단어가 모두 그룹 단어일 경우다.
- 따라서 그룹 단어가 아닌 경우일 때, n에서 1씩 빼주면서 개수를 구할 수 있다. 
"""