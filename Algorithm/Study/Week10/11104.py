n = int(input())

for _ in range(n):
    # 의미없는 0 지우기
    bi = int(input())
    # 2진수 10진수로 변환
    print(int(str(bi), 2))