# 1966
t = int(input())

for _ in range(t):
    N, M = map(int, input().split())
    array = list(map(int, input().split()))
    # 궁금한 문서의 위치를 추적하기 위한 새로운 배열 선언
    checkArray = [0 for _ in range(N)]
    # 궁금한 문서의 위치 설정
    checkArray[M] = True

    # 몇 번째로 출력되는지 세기 위한 변수
    count = 0
    while True:
        # print(array)
        # 중요도 배열의 첫 번째 요소가 최대값이라면 == 출력이 가능하다면
        if array[0] == max(array):
            # count 1 증가
            count += 1
            # 해당 요소가 궁금한 문서일 경우
            if checkArray[0]:
                print(count)
                break
            # 그렇지 않으면 첫 번째 요소 출력
            else:
                array.pop(0)
                checkArray.pop(0)
        # 중요도 배열의 첫 번째 요소가 최대값이 아니라면 첫 번째 요소를 뽑아 배열의 마지막으로 추가해준다.
        else:
            array.append(array.pop(0))
            checkArray.append(checkArray.pop(0))

"""
- 같은 크기의 새로운 배열(checkArray)를 만들고 궁금한 문서의 위치(M)를 True로 저장을 해준다.
- 그런 다음 중요도를 나타낸 배열과 새로운 배열을 같이 조작해준다.
"""