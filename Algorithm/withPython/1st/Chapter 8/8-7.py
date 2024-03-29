# 바닥 공사
# 정수 N을 입력 받기
n = int(input())

# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [0] * 1001

# 다이나믹 프로그래밍(Dynamic Programming) 진행 (보텀업)
d[1] = 1
d[2] = 3
for i in range(3, n + 1):
    d[i] = (d[i - 1] + 2 * d[i - 2]) % 796796

# 계산된 결과 출력
print(d[n])
print(d)

"""
- 다이나믹 프로그래밍 문제의 대부분은 그림을 그려서 점화식을 도출한 뒤 코드로 옮기는 과정이다.
- 반복문을 사용하는 보텀업 방식을 주로 사용한다.
- 이 문제 또한 다이나믹 프로그래밍의 대표적인 예제인 타일링 문제
접근 방법
세로 값이 2로 고정되어 있으므로 주어진 타일의 크기를 사용해 초깃값을 설정한다.
i번째 타일까지 채우려면 총 세 가지 경우가 있을 수 있다.
1) i-1번째 타일까지 채워져 있고 남은 타일을 채우는 경우 - 2X1 타일을 사용해서 채우는 방법
2) i-2번째 타일까지 채워져 있고 남은 타일을 채우는 경우 - 1X2 타일 두 개를 사용해서 채우는 방법
3) i-2번째 타일까지 채워져 있고 남은 타일을 채우는 경우 - 2X2 타일 하나를 사용해서 채우는 방법   
위 경우 외에는 고려할 필요가 없다 왜? 주어진 타일의 최대 크기가 2X2이기 때문에
따라서 위의 조건들로 점화식을 만들어서 문제에 주어진 796,796으로 나눈 값을 DP 테이블에 저장하면 최적의 해가 구해진다.
"""

