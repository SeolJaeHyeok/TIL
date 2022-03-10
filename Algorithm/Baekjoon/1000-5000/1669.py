import sys
input = sys.stdin.readline

monkey, dog = map(int, input().split())
dif = abs(monkey - dog) # 키 차이

if dif == 0: # 키 차이가 없는 경우 0 출력
    print(0)
else: # 키 차이가 있는 경우
    n = int(dif ** 0.5) # 키 차이의 제곱근

    if n ** 2 == dif: # n이 정수인 경우 계단식 증감
        print(2 * n - 1)
    else: # n이 정수가 아닌 경우
        z = dif - n ** 2 # 키 차이에서 n의 정수부를 제외
        if z <= n: # 그 값이 n보다 작으면 하루 추가
            print(2 * n)
        else: # n보다 크면 2일 추가
            print(2 * n + 1)