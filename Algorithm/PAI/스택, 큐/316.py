# Remove Duplicate Letters
# 재귀를 이용한 풀이
def removeDuplicateLetters(s):
    # 집합으로 정렬
    for char in sorted(s):
        suffix = s[s.index(char):]
        # 전체 집합과 접미사 집합이 일치할 때 분리 진행
        if set(s) == set(suffix):
            return char + removeDuplicateLetters(suffix.replace(char, ''))
    return ''

print(removeDuplicateLetters("bcabc"))
print(removeDuplicateLetters("cabcdcbc"))

# 스택을 이용한 풀이
from collections import Counter

def removeDuplicateLetters(s):
    counter, seen, stack = Counter(s), set(), []

    for char in s:
        counter[char] -= 1
        # 이미 처리된 문자열이라면 seen 집합에 추가가 되어있을테니 스킵
        if char in seen:
            continue
        # 뒤에 붙일 문자가 남아 있다면 스택에서 제거
        # 현재 문자가 스택에 쌓여있는 마지막 문자(바로 이전의 문자)보다 앞선 문자이고(char < stack[-1])
        # 해당 마지막 문자가 뒤에 더 남아있다면(counter[stack[-1]] > 0) 스택의 마지막 문자 제거
        while stack and char < stack[-1] and counter[stack[-1]] > 0:
            seen.remove(stack.pop())
        stack.append(char)
        seen.add(char)
        # print(stack)
        # print(seen)

    return ''.join(stack)

print(removeDuplicateLetters("bcabc"))
print(removeDuplicateLetters("cabcdcbc"))
