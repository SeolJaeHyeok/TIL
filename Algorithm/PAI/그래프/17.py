# Letter Combinations of a Phone Number
# dfs로 전체 탐색 후 백트래킹, 45ms
def letterCombinations(digits: str):
    def dfs(index, path):
        # 끝까지 탐색하면서 백트래킹
        if len(path) == len(digits):
            result.append(path)
            return

        # 입력값 자릿수 단위 반복
        for i in range(index, len(digits)):
            # 숫자에 해당하는 모든 문자열 반복
            for j in table[digits[i]]:
                dfs(i + 1, path + j)

    # 예외 처리
    if not digits:
        return []

    table = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
             "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
    result = []
    dfs(0, "")

    return result

print(letterCombinations("23"))

# 반복문으로 완전 탐색, 33ms
def letterCombinations(digits):
    table = {
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"]
    }

    if len(digits) == 1:
        return table[digits]
    elif not digits:
        return []
    else:
        ans = table[digits[0]]
        for i in range(1, len(digits)):
            first = ans
            another = table[digits[i]]
            result = []

            for f in first:
                for a in another:
                    result.append(f+a)
                ans = result

    return result


print(letterCombinations("23"))
