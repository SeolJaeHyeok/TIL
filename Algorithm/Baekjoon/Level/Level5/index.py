# 10818번
N = int(input())
nums = list(map(int, input().split()))
nums.sort()
print(nums[0], nums[-1])

# 2562번
# 1
nums = []
maxNum = 0
maxNumIdx = 0
for i in range(9):
    num = int(input())
    nums.append(num)

for j in range(len(nums)):
    if nums[j] > maxNum:
        maxNum = nums[j]
        maxNumIdx = j

print('{}\n{}'.format(maxNum, maxNumIdx + 1))

# 2
nums = []
for i in range(9):
    num = int(input())
    nums.append(num)
    maxNum = max(nums)
    maxNumIdx = nums.index(maxNum)

print('{}\n{}'.format(maxNum, maxNumIdx + 1))

# 2577번
# 1
A = int(input())
B = int(input())
C = int(input())
multipliedResult = list(str(A * B * C))
resultTable = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
Output = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range(len(multipliedResult)):
    for j in range(len(resultTable)):
        if int(multipliedResult[i]) == resultTable[j]:
            Output[j] += 1
for result in Output:
    print(result)

# 2
A = int(input())
B = int(input())
C = int(input())

mul = str(A*B*C)
result = [0] * 10

for i in range(len(mul)):
    result[int(mul[i])] += 1

for i in range(10):
    print(result[i])

# 3052번
# 1
lst = []

for i in range(10):
    num = int(input())
    lst.append(num % 42)

print(len(set(lst)))  # 집합 자료형 {} 은 중복을 허용하지 않기 때문에 서로 다른 수를 구할 때 용이

# 2
lst = []

for i in range(10):
    num = int(input()) % 42  # 42로 나눈 나머지 값이
    if not num in lst:  # 리스트 안에 없으면 추가 == 중복된 요소가 없으면 추가
        lst.append(num)

print(len(lst))

# 1546번
testNum = int(input())
scoreList = list(map(int, input().split()))
newList = []
maxScore = max(scoreList)

for i in range(len(scoreList)):
    newScore = scoreList[i] / maxScore*100
    newList.append(newScore)

avg = sum(newList) / testNum
print(avg)

# 8958번
N = int(input())
scoreList = []
for i in range(N):
    a = input()  # 문자열 입력 받고
    score = 0  # 반복문 한 번 돌면 초기화
    sumScore = 0
    for j in a:  # 입력받은 문자열을 한 글자씩 검사
        if j == 'O':  # 해당 문자열이 O면
            score += 1  # score +1, ex) 연속된 네 개의 O가 있으면 score 값의 변화는 1+1+1+1
        else:  # X를 만나면
            score = 0  # X를 만나면 score = 0으로 초기화하고 다음 글자 검사
        sumScore += score  # 한 글자씩 돌며 얻은 score를 sumScore에 더함, ex) OXOOXOOO일 때 score의 값 = 1+0+1+2+0+1+2+3
    scoreList.append(sumScore)

for score in scoreList:
    print(score)

# 4344번
C = int(input())

for i in range(C):
    nums = list(map(int, input().split()))  # 한 줄씩 입력 받고
    avg = sum(nums[1:]) / nums[0]  # nums[1:] = 각 테스트 케이스에서 학생들의 점수, nums[0] = 각 테스트 케이스의 학생 수
    moreThanAvgStudent = 0  # 평균을 넘는 학생 수
    for score in nums[1:]:  # 각 테스트 케이스의 학생의 점수를 반복문으로 돌아서
        if score > avg:  # 각 학생의 점수가 평균보다 높으면
            moreThanAvgStudent += 1  # 평균을 넘는 학생 수 1 증가
    rate = (moreThanAvgStudent / nums[0]) * 100  # 평균 넘는 학생 수를 전체 학생 수로 나눈 뒤 100을 곱해 비율 구하고
    print('{:.3f}%'.format(rate))  # 출력
