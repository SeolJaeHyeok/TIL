# 5622번
"""
문제
상근이의 할머니는 아래 그림과 같이 오래된 다이얼 전화기를 사용한다.
전화를 걸고 싶은 번호가 있다면, 숫자를 하나를 누른 다음에 금속 핀이 있는 곳 까지 시계방향으로 돌려야 한다.
숫자를 하나 누르면 다이얼이 처음 위치로 돌아가고, 다음 숫자를 누르려면 다이얼을 처음 위치에서 다시 돌려야 한다.
숫자 1을 걸려면 총 2초가 필요하다. 1보다 큰 수를 거는데 걸리는 시간은 이보다 더 걸리며, 한 칸 옆에 있는 숫자를 걸기 위해선 1초씩 더 걸린다.
상근이의 할머니는 전화 번호를 각 숫자에 해당하는 문자로 외운다. 즉, 어떤 단어를 걸 때, 각 알파벳에 해당하는 숫자를 걸면 된다. 예를 들어, UNUCIC는 868242와 같다.
할머니가 외운 단어가 주어졌을 때, 이 전화를 걸기 위해서 필요한 최소 시간을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 알파벳 대문자로 이루어진 단어가 주어진다. 단어의 길이는 2보다 크거나 같고, 15보다 작거나 같다.

출력
첫째 줄에 다이얼을 걸기 위해서 필요한 최소 시간을 출력한다.
"""

# 대문자 A~Z = 65~90
# 1
phoneNum = input()
time = 0

for i in range(len(phoneNum)):
    ascii_num = ord(phoneNum[i])
    if 65 <= ascii_num < 68:
        time += 3
    elif 68 <= ascii_num < 71:
        time += 4
    elif 71 <= ascii_num < 74:
        time += 5
    elif 74 <= ascii_num < 77:
        time += 6
    elif 77 <= ascii_num < 80:
        time += 7
    elif 80 <= ascii_num < 84:
        time += 8
    elif 84 <= ascii_num < 87:
        time += 9
    elif 87 <= ascii_num <= 90:
        time += 10

print(time)

# 2
phoneNum = input()  # ex) MILK
time = 0
dialTable = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

for i in range(len(phoneNum)):  # 4회 반복
    for dial in dialTable:  # ex) dial='MNO'
        if phoneNum[i] in dial:  # ex) phoneNum[i] = 'M', 'M'은 dial 안에 존재
            # 따라서 dialTable 안의 일치하는 dial의 인덱스를 찾아서 +3을 해주면 해당 숫자를 눌렀을 때 걸리는 시간
            # +3을 해주는 건 1을 눌렀을 때 2초가 걸린다고 했으므로 숫자 1 옆에 있는 테이블의 첫번 째 요소인 'ABC'=3초가 걸리고 한 칸 옆으로 갈 때마다 1초씩 증가
            time += dialTable.index(dial) + 3

print(time)
