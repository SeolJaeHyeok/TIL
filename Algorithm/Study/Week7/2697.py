# 다음 수 구하기
t = int(input())

for _ in range(t):
    num = list(input())

    flag = 0
    idx = 0
    for i in range(len(num) - 1, 0, -1):
        if num[i] > num[i - 1]:
            flag = 1
            idx = i - 1
            break
    # print(num[idx:])
    # print(num[:idx])
    if not flag:
        print('BIGGEST')
        continue
    else:
        behind = num[idx:]
        front = num[:idx]
        target = int(behind[0])
        tmp_num = 10
        for j in range(len(behind)):
            if target < int(behind[j]) < tmp_num:
                tmp_num = int(behind[j])
        # print(behind)
        tmp_idx = behind.index(str(tmp_num))
        behind[tmp_idx], behind[0] = behind[0], str(tmp_num)
        # print(behind)
        answer = ''.join(front + [str(tmp_num)] + sorted(behind[1:]))
        print(answer)





