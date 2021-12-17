"""
참조: https://rccode.tistory.com/entry/Python-%EB%B0%B1%EC%A4%80-12970%EB%B2%88-AB?category=1186954?category=1186954
"""
n, k = map(int, input().split())

words = ['B'] * n
aCount = 0
curK = 0
lastAIdx = -1 # 뒤에서부터 A를 하나씩 앞으로 밀기 위한 인덱스, 초기값은 마지막 인덱스
while curK < k:
    targetIdx = n - 1 - (aCount + 1) # 추가해야할 A의 인덱스
    # k개의 쌍을 만들었다면 탈출
    if curK == k:
        break
    if lastAIdx < aCount: # A를 추가하는 부분
        # 추가해야할 위치의 값이 A라면 n개의 문자로 k개의 쌍을 만들지 못한다는 의미이므로 탈출
        if words[targetIdx] == 'A':
            words.clear()
            break
        else: # 그렇지 않다면 A를 추가하고 마지막 A의 위치를 갱신
            words[targetIdx] = 'A'
            lastAIdx = targetIdx
            curK += 1
            aCount += 1
    else: # A를 앞으로 미는 부분
        words[lastAIdx] = 'B'
        words[lastAIdx-1] = 'A'
        lastAIdx -= 1
        curK += 1

if words:
    print("".join(words))
else:
    print("-1")
