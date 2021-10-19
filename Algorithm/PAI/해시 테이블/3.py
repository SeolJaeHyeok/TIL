# Longest Substring Without Repeating Characters
# 투 포인터와 슬라이딩 윈도우로 사이즈 조절, 71ms
def lengthOfLongestSubstring(s: str) -> int:
    used = {}
    max_length = start = 0

    for index, char in enumerate(s):
        # 이미 등장했던 문자라면 'start' 위치 갱신
        if char in used and start <= used[char]:
            start = used[char] + 1
        else: # 최대 부분 문자열 길이 갱신
            max_length = max(max_length, index - start + 1)

        # 현재 문자의 위치 삽입
        used[char] = index

    return max_length


print(lengthOfLongestSubstring("abcabcbb"))
print(lengthOfLongestSubstring("bbbbb"))
print(lengthOfLongestSubstring("pwwkew"))

"""
- 투 포인터를 이용하면 될 것 같다는 생각이 들었지만 구체적인 구현은 성공하지 못했다.
- 슬라이딩 윈도우와 투 포인터 기법은 굉장히 자주 사용이 되니까 꼭 막힘없이 구현할 수 있을 정도로 만들어야지..

투 포인터 기법은 시작과 끝 두개의 포인터를 놓고 양쪽으로 이동하면서 탐색하는 기법이고
슬라이딩 윈도우는 고정된 윈도우 사이즈를 가지고 윈도우을 이동시키면서 탐색하는 기법이다.  
"""