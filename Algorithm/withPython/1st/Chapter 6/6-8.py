# 성적이 낮은 순서로 학생 출력하기
# my
n = int(input())

array = []
for i in range(n):
    array.append(tuple(map(str, input().split())))


def setting(data):
    return data[1]


array = sorted(array, key=setting)

print(array)

# sol
n = int(input())

array = []
for i in range(n):
    input_data = input().split()
    array.append((input_data[0], int(input_data[1])))


array = sorted(array, key=lambda student: student[1])

print(array)
