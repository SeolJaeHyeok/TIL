# Jewels and Stones
# 해시 테이블 이용한 풀이(1), 28ms, 10줄
def numJewelsInStones(jewels: str, stones: str) -> int:
    table = {}
    count = 0
    for jewel in jewels:
        table[jewel] = jewel

    for stone in stones:
        if stone in table:
            count += 1

    return count


print(numJewelsInStones("aA", "aAAbbbb"))
print(numJewelsInStones("z", "ZZ"))


# 해시 테이블 이용한 풀이(2), 74ms, 14줄
def numJewelsInStones(jewels: str, stones: str) -> int:
    table = {}

    for stone in stones:
        if stone not in table:
            table[stone] = 1
        else:
            table[stone] += 1

    count = 0
    for jewel in jewels:
        if jewel in table:
            count += table[jewel]

    return count


print(numJewelsInStones("aA", "aAAbbbb"))
print(numJewelsInStones("z", "ZZ"))

# defaultDict를 이용한 풀이, 32ms, 10줄
from collections import defaultdict, Counter

def numJewelsInStones(jewels: str, stones: str) -> int:
    table = defaultdict(int)
    count = 0

    # 비교 없이 돌 빈도 수 계산
    for stone in stones:
        table[stone] += 1

    # 비교 없이 보석 빈도 수 합산
    for jewel in jewels:
        count += table[jewel]

    return count


print(numJewelsInStones("aA", "aAAbbbb"))
print(numJewelsInStones("z", "ZZ"))


# Counter로 계산 생략, 32ms, 7줄
def numJewelsInStones(jewels: str, stones: str) -> int:
    freqs = Counter(stones)
    count = 0

    # 비교 없이 보석 빈도수 합산
    for jewel in jewels:
        count += freqs[jewel]

    return count


print(numJewelsInStones("aA", "aAAbbbb"))
print(numJewelsInStones("z", "ZZ"))


# Pythonic Way, 61ms, 1줄 
def numJewelsInStones(jewels: str, stones: str) -> int:

    return sum(stone in jewels for stone in stones)


print(numJewelsInStones("aA", "aAAbbbb"))
print(numJewelsInStones("z", "ZZ"))
