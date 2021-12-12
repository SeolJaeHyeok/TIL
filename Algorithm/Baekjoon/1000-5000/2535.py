# 아시아 정보 올림피아드
n = int(input())
array = []
for _ in range(n):
    numN, numS, score = map(int, input().split())
    array.append((numN, numS, score))

# 점수가 높은 순서대로 정렬
array.sort(key=lambda x: x[2], reverse=True)

# 1등과 2등 결과 배열에 추가
result = [(array[0][0], array[0][1]), (array[1][0], array[1][1])]

# 세번째 요소부터 순회
for i in range(2, len(array)):
    # 1등과 2등의 국가가 같은 경우
    if result[0][0] == result[1][0]:
        # 3등이 1등과 2등의 국가와 같지 않은 경우 결과 배열에 추가하고 탈출
        if array[i][0] != result[0][0] and array[i][0] != result[1][0]:
            result.append((array[i][0], array[i][1]))
            break
        # 3등이 1등과 2등의 국가와 같다면 스킵
        else:
            continue
    # 1등과 2등의 국가가 같지 않은 경우 결과 배열에 추가하고 탈출
    else:
        result.append((array[i][0], array[i][1]))
        break

# 국가번호와 학생 번호 출력
for nation, student in result:
    print(nation, student)




