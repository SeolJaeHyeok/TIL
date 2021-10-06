# 1764
# 시간 초과
n, m = map(int, input().split())

a = set(input() for i in range(n))
b = set(input() for i in range(m))

result = list(a & b)
result.sort()

print(len(result))
for i in result:
    print(i)

"""
- 중복된 자료들을 필터링 할 때는 set 자료형을 활용하여 필터링
- 교집합 차집합 합집합 등의 수학적인 개념 적용이 가능하여 편리하게 구현할 수 있음
"""



