import sys
input = sys.stdin.readline

n = int(input())

stack = []
answer = []
flag = True
count = 1 # 오름차순으로 스택에 추가될 수
for i in range(n):
    num = int(input())

    # 입력받은 수보다 작을 때까지 추가
    while count <= num:
        stack.append(count)
        answer.append('+')
        count += 1

    # 스택의 마지막으로 들어온 수가 입력 받은 수와 같으면 스택에서 꺼내기
    if stack[-1] == num:
        stack.pop()
        answer.append('-')
    else: # 다르면 flag 처리
        flag = False

if flag:
    for i in answer:
        print(i)
else:
    print('NO')