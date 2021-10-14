# Group Anagrams
# defaultdict 자료형 이용해서 구현
from collections import defaultdict

def groupAnagrams(p):
    array = defaultdict(list)
    for word in p:
        array[''.join(sorted(word))].append(word)

    return array.values()

input_data = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(input_data))

"""
- 애너그램은 구성하는 알파벳의 종류 및 개수가 동일한 단어를 말한다.
- defaultdict 자료형의 default 값을 리스트로 주어 키 에러가 발생하지 않게 만들고
- 각 단어의 알파벳을 정렬하고 join 메서드를 사용하여 하나의 단어로 합친 다음 그 값을 키로 하여 추가
ex) 'eat' -> 'aet', 'tea' -> 'aet'
'aet'를 키 값으로 하여 추가하면 동일한 키를 가지고 있는 단어들이 리스트 원소로 추가 

- sorted() 함수는 정렬된 결과를 별도로 리스트로 리턴
- sort() 메서드는 제자리 정렬이라고 부르기도 하는데, 정렬된 결과를 별도로 리턴하지 않고 입력을 출력으로 덮어 쓴다.
"""


#