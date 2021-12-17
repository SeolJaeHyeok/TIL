"""
가장 긴 증가하는 부분 수열(LIS) 여러 유형 정리
참조 : https://seohyun0120.tistory.com/entry/%EA%B0%80%EC%9E%A5-%EA%B8%B4-%EC%A6%9D%EA%B0%80%ED%95%98%EB%8A%94-%EB%B6%80%EB%B6%84-%EC%88%98%EC%97%B4LIS-%EC%99%84%EC%A0%84-%EC%A0%95%EB%B3%B5-%EB%B0%B1%EC%A4%80-%ED%8C%8C%EC%9D%B4%EC%8D%AC
"""
# 1, 11053
n = int(input())

array = list(map(int, input().split())) # ex) [10, 20, 10, 30, 20, 50]

dp = [1 for i in range(n)] # dp 테이블 모두 1로 초기화, array[i]를 마지막 원소로 가질 때 가장 긴 증가하는 부분 수열의 길이

for i in range(n):
    for j in range(i):
        # 현재 값보다 현재 값 이전의 값이 작다면
        if array[i] > array[j]:
            # 현재 위치 이전의 값들 중 최대값(가장 큰 부분 수열의 길이)에 1을 더해준다
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
