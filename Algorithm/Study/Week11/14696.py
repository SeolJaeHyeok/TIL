from collections import defaultdict

n = int(input())
for _ in range(n):
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # 입력 개수 제거
    A.pop(0)
    B.pop(0)

    A_dic = defaultdict(int)
    B_dic = defaultdict(int)

    for num in A:
        A_dic[num] += 1
    for num in B:
        B_dic[num] += 1

    # 우선 순위가 높은 모양부터 비교
    # 모두 같을 경우 D 출력
    for shape in range(4, 0, -1):
        if A_dic[shape] > B_dic[shape]:
            print('A')
            break
        elif A_dic[shape] < B_dic[shape]:
            print('B')
            break
    else:
        print('D')
