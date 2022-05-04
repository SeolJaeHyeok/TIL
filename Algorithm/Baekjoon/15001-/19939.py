import sys
input = sys.stdin.readline

n, k = map(int, input().split())

# 1 ~ k까지의 합 = 최소한으로 필요한 공의 개수
d = k * (k + 1) // 2 # 공차가 1인 등차수열의 합

if n < d: # n이 d보다 작을 경우
    # 바구니에 공을 전부 담을 수 없다
    print(-1)
elif (n - d) % k == 0: # n - d가 k로 나누어 떨어질 경우
    # n이 몇개가 되든 각 바구니에 동일하게 공이 추가되므로
    # 최대값과 최소값의 차이는 동일하게 유지
    print(k - 1)
else: # n - d가 k로 나누어떨어지지 않을 경우
    # 가장 큰 바구니부터 하나씩 채워넣으면 되므로
    # 최대값과 최소값의 차이는 ((k + 1) - 1) = k
    print(k)

"""
공을 최소한으로 담기 위해서는 각 바구니의 차이가 1이 되어야 한다.

각 바구니에는 1개 이상의 공이 들어가야 하므로
그렇게 만들기 위해서 최소한으로 필요한 공의 개수는 공차가 1인 등차수열의 합 k*(k+1) / 2이 된다.

따라서 최소한으로 필요한 공의 개수보다 작으면 모든 바구니에 다른 수에 공이 담길 수 없으므로 조건에 맞지 않고
주어진 공의 개수에서 최소한의 공의 개수의 차를 바구니의 수로 나눠 나머지가 0인지 여부에 따라 다르게 처리 가능
"""
