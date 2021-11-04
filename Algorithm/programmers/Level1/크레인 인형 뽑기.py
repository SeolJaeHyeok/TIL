# 36/100
def solution(board, moves):
    # board 전처리 -> array[0]은 첫 번째 칸, array[1]은 두 번째 칸
    # (moves에서 들어오는 수 - 1)의 인덱스에서 인형을 뽑아서 스택에 추가하면 됌
    array = [[] * len(board) for _ in range(len(board))]
    for i in range(len(board)):
        for j in range(len(board)):
            array[i].append(board[j][i])

    stack = []
    answer = 0
    for move in moves:
        for i in range(len(array[move - 1])):
            now = array[move - 1][i]
            if now == 0:
                continue
            else:
                stack.append(now)
                array[move - 1][i] = 0
                if len(stack) >= 2 and stack[-1] == stack[-2]:
                    stack = stack[:-2]
                    answer += 2
                break # -> 이게 문제였다..
            # break -> 여기서 해줘야 move 하나 당 한 개의 인형만 뽑을 수 있는 건데 이상한 데서 해주니 move마다 모든 인형들을 뽑은 것

    return answer


# 100/100
def solution(board, moves):
    # board 전처리 -> array[0]은 첫 번째 칸, array[1]은 두 번째 칸
    # (moves에서 들어오는 수 - 1)의 인덱스에서 인형을 뽑아서 스택에 추가하면 됌
    array = [[] * len(board) for _ in range(len(board))]
    for i in range(len(board)):
        for j in range(len(board)):
            array[i].append(board[j][i])

    stack = []
    answer = 0
    for move in moves:
        for i in range(len(array[move - 1])):
            now = array[move - 1][i]
            if now == 0:
                continue
            else:
                stack.append(now)
                array[move - 1][i] = 0
                if len(stack) >= 2 and stack[-1] == stack[-2]:
                    stack = stack[:-2]
                    answer += 2
            break

    return answer


# 100/100
def solution(board, moves):
    stack = []
    answer = []
    for move in moves:
        for i in range(len(board)):
            now = board[i][move - 1]
            if now > 0:
                stack.append(now)
                board[i][move - 1] = 0
                if stack[-1:] == stack[-2:-1]:
                    answer += stack[-1:]
                    stack = stack[:-2]
                break

    return len(answer) * 2
