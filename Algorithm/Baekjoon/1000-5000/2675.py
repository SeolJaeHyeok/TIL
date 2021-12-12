# 2675번
"""
문제
문자열 S를 입력받은 후에, 각 문자를 R번 반복해 새 문자열 P를 만든 후 출력하는 프로그램을 작성하시오.
즉, 첫 번째 문자를 R번 반복하고, 두 번째 문자를 R번 반복하는 식으로 P를 만들면 된다. S에는 QR Code "alphanumeric" 문자만 들어있다.
QR Code "alphanumeric" 문자는 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ\$%*+-./: 이다.

입력
첫째 줄에 테스트 케이스의 개수 T(1 ≤ T ≤ 1,000)가 주어진다. 각 테스트 케이스는 반복 횟수 R(1 ≤ R ≤ 8), 문자열 S가 공백으로 구분되어 주어진다.
S의 길이는 적어도 1이며, 20글자를 넘지 않는다.

출력
각 테스트 케이스에 대해 P를 출력한다
"""
nums = int(input())  # 테스트 케이스 개수

for i in range(nums):
    R = list(map(str, input().split()))  # 반복 횟수와 문자를 리스트 형태로 입력 받음 ex) ['5', 'ABC']
    word = R[1:][0]  # 입력한 문자 ex) 'ABC'
    for j in word:  # 'A', 'B', 'C'
        newWord = j*int(R[0])  # 한 문자씩 반복횟수와 곱해서 ex) 'A'*5 => 'B'*5 => 'C'*5
        print(newWord, end='')  # 한 줄에 출력 ex) AAA + BBB + CCC
    print()  # 끝나면 줄 바꿈
