# Most Common Word
# Counter 객체 이용
import re
from collections import Counter

def mostCommonWord(p: str, b: list):
    array = [word for word in re.sub(r'[^\w]', ' ', p).lower().split() if word not in b]
    return Counter(array).most_common(1)[0][0]


paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

result = mostCommonWord(paragraph, banned)
print(result)


# defaultDict 이용
import re
import collections

def mostCommonWord(p: str, b: list):
    array = [word for word in re.sub(r'[^\w]', ' ', p).lower().split() if word not in b]
    counts = collections.defaultdict(int)

    for a in array:
        counts[a] += 1

    return max(counts, key=counts.get)


paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

result = mostCommonWord(paragraph, banned)
print(result)

"""
- 정규식에서 \w는 단어 문자를 뜻하며, ^는 not을 의미한다. 따라서 위 정규식은 단어 문자가 아닌 모든 문자를 공백으로 치환하는 역할을 한다.
- defaultDict 자료형을 선언할 때 int 기본값이 자동으로 부여되게 선언.
따라서 여기서는 키 존재 유무를 확인할 필요 없이 즉시 counts[a] += 1을 수행할 수 있다. 

"""