# 우테코 2기 7번
def solution(s):
    array = list(s)
    check = True
    while check:
        check = False
        cur_string = array

        for i in range(len(array) - 1):
            if array[i] == array[i + 1]:
                cur_string.pop(i + 1)
                cur_string.pop(i)
                check = True
                break

        array = cur_string

    if len(array) > 0:
        return ''.join(array)
    else:
        return ""


print(solution("browoanoommnaon"))
print(solution("zyelleyz"))