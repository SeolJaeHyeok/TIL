# 우테코 2기 4번
# 그냥 날코딩으로 풀었는데 더 좋은 방법 있을까
def solution(pobi, crong):
    array = [pobi, crong]

    # 올바른 페이지 번호가 아닌 경우
    if pobi[1] - pobi[0] != 1 or crong[1] - crong[0] != 1:
        return -1

    result = []
    # 포비와 크롱 순서대로 합계 구하기
    for left, right in array:
        total = 1
        # 오른쪽 페이지가 10으로 나누어 떨어질 경우
        if right % 10 == 0:
            # 오른쪽 페이지가 10 또는 20이라면 왼쪽 페이지 더하기
            if right == 10 or right == 20 or right == 110 or right == 120\
                    or right == 210 or 220 or right == 310 or right == 320:
                for s in str(left):
                    total += int(s)
                total -= 1
            # 아니면 곱하기
            else:
                for s in str(left):
                    total *= int(s)
        # 기본적으로 오른쪽 페이지가 100 단위가 아니면 무조건 오른쪽 페이지의 값이 더하기든 곱하기든 더 크다
        # 더할 경우가 곱할 경우보다 큰 숫자인 범위
        elif 100 < right < 122 or 200 < right <= 212 or 300 < right <= 311:
            for s in str(right):
                total += int(s)
            total -= 1
        # 곱할 경우가 더 큰 숫자인 범위
        else:
            for s in str(right):
                total *= int(s)
        # 포비, 크롱 순으로 결과 배열에 추가
        result.append(total)

    if result[0] > result[1]: # 포비가 더 큰 경우
        return 1
    elif result[0] < result[1]: # 크롱이 더 큰 경우
        return 2
    else: # 비기는 경우
        return 0


print(solution([109, 110], [119, 120]))
print(solution([9, 10], [19, 20]))
print(solution([209, 210], [219, 220]))
print(solution([309, 310], [319, 320]))
print(solution([97, 98], [297, 298]))
print(solution([97, 98], [197, 198]))
print(solution([131, 132], [211, 212]))
print(solution([99, 100], [211, 212]))
print(solution([99, 102], [211, 212]))


# 함수 만들어서 풀이 -> 이게 훨씬 더 깔끔하고 가독성도 좋다. 날코딩 풀이도 아님
def sum(li):
    left_sum = right_sum = 0

    # 왼쪽 페이지의 더하기 합계
    for s in str(li[0]):
        left_sum += int(s)

    # 오른쪽 페이지의 더하기 합계
    for s in str(li[1]):
        right_sum += int(s)

    return max(left_sum, right_sum)


def mul(li):
    left_mul = right_mul = 1

    # 왼쪽 페이지의 곱하기 합계
    for s in str(li[0]):
        left_mul *= int(s)

    # 오른쪽 페이지의 곱하기 합계
    for s in str(li[1]):
        right_mul *= int(s)

    return max(left_mul, right_mul)


def solution(pobi, crong):
    # 올바른 페이지 번호가 아닌 경우
    if pobi[1] - pobi[0] != 1 or crong[1] - crong[0] != 1:
        return -1

    pobi_sum = sum(pobi)
    pobi_mul = mul(pobi)
    pobi_max = max(pobi_sum, pobi_mul)

    crong_sum = sum(crong)
    crong_mul = mul(crong)
    crong_max = max(crong_sum, crong_mul)

    if crong_max < pobi_max:
        return 1
    elif crong_max > pobi_max:
        return 2
    else:
        return 0


print(solution([109, 110], [119, 120]))
print(solution([9, 10], [19, 20]))
print(solution([209, 210], [219, 220]))
print(solution([309, 310], [319, 320]))
print(solution([97, 98], [297, 298]))
print(solution([97, 98], [197, 198]))
print(solution([131, 132], [211, 212]))
print(solution([99, 100], [211, 212]))
print(solution([99, 102], [211, 212]))