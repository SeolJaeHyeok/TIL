# 국영수
n = int(input())

array = []
for _ in range(n):
    array.append(tuple(input().split()))

print(array)
"""
정렬 기준
1) 두 번째 원소를 기준으로 내림차순 정렬
2) 두 번째 원소가 같을 경우, 세 번째 원소를 기준으로 오름차순 정렬
3) 세 번째 원소가 같을 경우. 네 번째 원소를 기준으로 내림차순 정렬
4) 모든 원소가 같을 경우, 첫 번째 원소를 기준으로 오름차순 정렬
"""
array.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for i in array:
    print(i[0])

# 12
# Junkyu 50 60 100
# Sangkeun 80 60 50
# Sunyoung 80 70 100
# Soong 50 60 90
# Haebin 50 60 100
# Kangsoo 60 80 100
# Donghyuk 80 60 100
# Sei 70 70 70
# Wonseob 70 70 90
# Sanghyun 70 70 80
# nsj 80 80 80
# Taewhan 50 60 90

"""
- 튜플 자료형을 정렬하게 되면 모든 원소가 첫 번째 원소의 순서에 맞게 정렬되고, 첫 번째 원소의 값이 같은 경우 두 번째 원소의 순서에 맞게 정렬되고
두 번째 원소의 값이 같으면 세 번째 원소의 순서에 맞게 정렬된다.
- 이처럼 튜플 자료형은 알아서 원소의 순서대로 정렬이 이뤄지기 때문에 sort 함수를 사용할 때 key에 넘겨줄 람다 함수에서 튜플의 형태로 정렬 조건을 넘겨주면
그에 맞게끔 정렬이 알아서 이뤄진다.
- 내림차순으로 정렬하고 싶으면 앞에 -를 붙여주면 된다.
"""