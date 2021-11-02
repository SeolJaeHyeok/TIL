def solution(arr1, arr2):
    answer = [[] * len(arr1) for _ in range(len(arr1))]
    print(answer)
    for i in range(len(arr1)):
        for j in range(len(arr1[0])):
            answer[i].append(arr1[i][j] + arr2[i][j])

    return answer