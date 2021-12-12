t = int(input())

for _ in range(t):
    n = int(input())
    array = list(map(int, input().split()))
    d = [0] * n
    d[0] = array[0]
    # 연속하는 부분 배열이므로 이전 값에서 현재 값을 더한 값(d[i-1]+array[i])과 현재 값(array[i])을 비교하여 더 큰 값 저장
    for i in range(1, len(array)):
        d[i] = max(d[i-1] + array[i], array[i])

    print(max(d))
