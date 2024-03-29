# 실수 자료형

# 10억의 지수 표현 방식
a = 1e9
print(a)

# 752.5
a = 75.25e1
print(a)

# 3.954
a = 3954e-3
print(a)

# round(실수형 데이터, (반올림하고자 하는 위치 - 1))
print(round(123.456, 2))
print(round(123.456, 1))
print(round(123.456))

############################################

# 리스트 자료형

# 크기가 N이고, 모든 값이 0인 1차원 리스트 선언
n = 10
a = [0] * n
print(a)
a = [0 for i in range(10)]
print(a)
a = [0 for _ in range(10)]
print(a)

# 리스트 컴프리헨션

# 0부터 19까지의 수 중에서 홀수만 포함하는 리스트
a = [i for i in range(20) if i % 2 != 0]
print(a)

# 1부터 9까지의 수의 제곱 값을 포함하는 리스트
a = [i*i for i in range(1, 10)]
print(a)

# N x M 크기의 2차원 리스트 초기화
# 참고로 특정 크기의 2차원 리스트를 초기화할 때는 반드시 리스트 컴프리헨션을 사용해야 한다.
n = 3
m = 3
a = [[0] * m for _ in range(n)]
print(a)

# N x M 크기의 2차원 리스트 초기화(잘못된 방법)
# 이렇게 2차원 리스트를 초기화하면 의도하지 않은 결과가 나올 수 있다.
n = 3
m = 4
a = [[0] * m] * n
print(a)

a[1][1] = 5
print(a)
"""
실행결과를 보면 a[1][1]의 값만 5로 바꿨을 뿐인데 3개의 리스트의 1번째 인덱스의 해당하는 원소들의 값이 모두 5로 바뀐 것을 확인할 수 있다.
이는 내부적으로 포함된 4개의 리스트가 모두 동일한 객체에 대한 3개의 레퍼런스로 인식되기 때문이다.
따라서 특정한 크기를 가지는 2차원 리스트를 초기화할 때에는 리스트 컴프리헨션을 이용해서 초기화 하도록 하자.
"""


