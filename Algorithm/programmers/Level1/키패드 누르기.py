# 몫과 나머지 연산으로 이동 거리 계산
def solution(numbers, hand):
    answer = ''
    left, right = 10, 12
    for num in numbers:
        if num == 0:
            num = 11

        if num % 3 == 1:  # 1, 4, 7이 입력되면 왼손으로 누르기
            answer += 'L'
            left = num
        elif num % 3 == 0:  # 3, 6, 9가 입력되면 오른손으로 누르기
            answer += 'R'
            right = num
        else:  # 2, 5, 8, 0이 입력되면
            # 이동할 칸 수 계산
            nL = abs(left - num)
            nR = abs(right - num)
            l = (nL // 3) + (nL % 3)
            r = (nR // 3) + (nR % 3)
            if l > r:  # 왼손이 더 많이 이동하면 오른손으로 입력
                answer += 'R'
                right = num
            elif l < r:  # 오른손이 더 많이 이동하면 왼손으로 입력
                answer += 'L'
                left = num
            else:  # 이동 거리가 같으면 hand에 따라 입력
                if hand == 'left':
                    answer += 'L'
                    left = num
                else:
                    answer += 'R'
                    right = num

    return answer


# 모든 키패드 미리 선언 후 이동 거리 계산
def solution(numbers, hand):
    answer = ''
    key_dict = {
        1: (0, 0), 2: (0, 1), 3: (0, 2),
        4: (1, 0), 5: (1, 1), 6: (1, 2),
        7: (2, 0), 8: (2, 1), 9: (2, 2),
        10: (3, 0), 0: (3, 1), 12: (3, 2)
    }

    left = [1, 4, 7]
    right = [3, 6, 9]
    lhand = 10
    rhand = 12
    for i in numbers:
        if i in left:
            answer += 'L'
            lhand = i
        elif i in right:
            answer += 'R'
            rhand = i
        else:
            curPos = key_dict[i]
            lPos = key_dict[lhand]
            rPos = key_dict[rhand]
            ldist = abs(curPos[0]-lPos[0]) + abs(curPos[1]-lPos[1])
            rdist = abs(curPos[0]-rPos[0]) + abs(curPos[1]-rPos[1])

            if ldist < rdist:
                answer += 'L'
                lhand = i
            elif ldist > rdist:
                answer += 'R'
                rhand = i
            else:
                if hand == 'left':
                    answer += 'L'
                    lhand = i
                else:
                    answer += 'R'
                    rhand = i

    return answer