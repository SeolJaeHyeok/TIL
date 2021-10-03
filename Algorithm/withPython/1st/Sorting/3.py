def solution(N, stages):
    answer = []
    length = len(stages)  # 사용자의 수

    for i in range(1, N + 1):
        count = stages.count(i)  # 해당 단계에 머물고 있는 사용자의 수

        if length == 0:
            fail = 0
        else:
            fail = count / length

        answer.append((i, fail))  # 해당 스테이지와 실패율 추가
        length -= count  # 사용자 수 갱신
    # print(answer)
    answer.sort(key=lambda x: x[1], reverse=True)
    answer = [i[0] for i in answer]
    # print(answer)
    return answer


if __name__ == '__main__':
    assert solution(5, [2, 1, 2, 6, 2, 4, 3, 3]) == [3, 4, 2, 1, 5]
    assert solution(4, [4, 4, 4, 4, 4]) == [4, 1, 2, 3]
    print('OK')


"""
풀이 방법
- 1번째 스테이지부터 N번째 스테이지까지 각각의 스테이지 번호와 실패율을 구해서 내림차순으로 정렬
- 해당 스테이지를 클리어하지 못한 플레이어의 수는 해당 스테이지 번호와 같은 수의 갯수와 같다. -> count 함수 이용
- 스테이지에 도달한 플레이어의 수는 length 변수를 이용해 스테이지가 진행됨에 따라 갱신해주면서 사용
- 1단계 stage의 length(해당 스테이지에 도달한 플레이어 수)는 입력된 stages의 길이와 같고 
단계가 진행됨에 따라 해당 스테이지의 머물러 있던 사람들을 빼면서 값을 갱신해 간다.   
"""