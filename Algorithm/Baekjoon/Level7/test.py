def solution(param0):
    answer = ''
    typeTable = ["BOOL", "SHORT", "FLOAT", "INT", "LONG"]
    paddingTable = ['.', '..', '...', '....', '.....', '......', '.......']
    memorySize = 128

    if memorySize > 128:
        answer = 'HALT'

    for i in range(len(param0)):
        for j in range(len(typeTable)):
            if param0[j] == 'BOOL':
                answer = '#'
                '.'.join(answer)
                memorySize -= 1
            elif param0[j] == 'SHORT':
                answer = '##'
                memorySize -= 2
            elif param0[j] == 'FLOAT':
                answer = '####'
                memorySize -= 4
            elif param0[j] == 'INT':
                answer = '########'
                memorySize -= 8
            else:
                answer = '########,########'
                memorySize -= 16

    return answer


print(solution(["INT", "INT", "BOOL", "SHORT", "LONG"]))

