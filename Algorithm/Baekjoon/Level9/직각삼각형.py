# 4153번
"""
문제
과거 이집트인들은 각 변들의 길이가 3, 4, 5인 삼각형이 직각 삼각형인것을 알아냈다. 주어진 세변의 길이로 삼각형이 직각인지 아닌지 구분하시오.
입력
입력은 여러개의 테스트케이스로 주어지며 마지막줄에는 0 0 0이 입력된다.
각 테스트케이스는 모두 30,000보다 작은 양의 정수로 주어지며, 각 입력은 변의 길이를 의미한다.

출력
각 입력에 대해 직각 삼각형이 맞다면 "right", 아니라면 "wrong"을 출력한다.

풀이방법
1) 직각 삼각형은 "대각선의 제곱 == 남은 두 변의 제곱의 합" 이기 때문에 먼저 리스트로 세 개의 숫자를 받는다.
2) 먼저 0 0 0이 입력되면 프로그램이 종료되어야하므로 세 수의 합이 0일 때 반복문 탈출하며 종료
3) 그렇지 않다면 세 숫자 중 최대값을 구해 저장한 다음 리스트에서 제거하고 위의 식을 이용해서 결과를 출력
"""


def powCalculator(num):  # 제곱을 리턴하는 함수
    return pow(num, 2)


while 1:
    num_list = list(map(int, input().split()))
    if sum(num_list) == 0:
        break
    max_num = max(num_list)
    num_list.remove(max_num)
    if powCalculator(max_num) == powCalculator(num_list[0]) + powCalculator(num_list[1]):
        print('right')
    else:
        print('wrong')


