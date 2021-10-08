# 4673
def d(n):
    # 해당 숫자와 해당 숫자의 각 자리수를 더하여 리턴
    for i in str(n):
        n += int(i)
    return n

# 전체 범위를 설정
numbers = set(range(1, 10001))
# 셀프 넘버가 아닌 숫자 == 생성자가 있는 숫자를 담을 집합, 겹치는 숫자는 중복 허용 x
generated_numbers = set()

# 범위 내의 모든 숫자를 함수에 전달 후 집합에 추가
for num in numbers:
    generated_num = d(num)
    generated_numbers.add(generated_num)

# 전체 범위 - 셀프 넘버가 아닌 숫자 = 셀프 넘버의 숫자
self_numbers = numbers - generated_numbers
# 집합 자료형은 순서가 보장되지 않기 때문에 정렬 후 출력
for i in sorted(self_numbers):
    print(i)