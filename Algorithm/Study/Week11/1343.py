board = input()

# 문자열 대치, replace('oldValue', 'newValue')
answer = board.replace('XXXX', 'AAAA')
answer = answer.replace('XX', 'BB')

if 'X' in answer:
    print(-1)
else:
    print(answer)

