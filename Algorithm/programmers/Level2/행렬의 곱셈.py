def solution(arr1, arr2):
    answer = []

    for i in range(len(arr1)):
        tmp = []
        for j in range(len(arr2[0])):
            t = 0
            for k in range(len(arr1[0])):
                t += arr1[i][k] * arr2[k][j]
            tmp.append(t)
        answer.append(tmp)

    return answer


# zip 함수 공부 하자 
def productMatrix(A, B):
    return [[sum(a*b for a, b in zip(A_row,B_col)) for B_col in zip(*B)] for A_row in A]

a = [[2, 3, 2], [4, 2, 4], [3, 1, 4]]
b = [[5, 4, 3], [2, 4, 1], [3, 1, 1]]
print(productMatrix(a, b))
