import sys, math

# divide : 순열의 길이가 whole이고 num번째인 순열을 출력하는 함수
# 		   basket : 집합번호를 담는 리스트
def divide(num, whole, basket):
	# 한자리를 빼고 다 뽑은 경우
    if whole == 1:
    	# vis : 중복을 막기 위해 방문체크하는 배열
        vis = [False] * (n + 1)
        # permu : 실제 수열
        permu = []
        # 각 자리수별 집합 번호를 순회한다
        for i in ans:
        	# cnt : 몇번째 집합인가를 판단하는 변수
            cnt = 0
            for j in range(1, n + 1):
            	# 현재 수가 한번도 방문하지 않았다면 cnt 증가
                if vis[j] == False:
                    cnt += 1
                # 현재 j의 집합 번호가 현재의 집합번호와 같다면 실제 순열에 j를 추가한 후
                # 반복문을 빠져 나온다
                if cnt == i:
                    permu.append(j)
                    vis[j] = True
                    break
        # 한번도 사용하지 않은 수가 수열의 마지막 자리이므로 더한다
        for i in range(1, n + 1):
            if vis[i] == False:
                permu.append(i)
        # 실제 순열 출력
        print(' '.join(map(str, permu)))
        return
    # 아직 다 뽑지 않았다면 한 집합의 크기(temp)를 미리 구한다
    temp = math.factorial(whole - 1)
    # 만일 num이 나누어 떨어지지 않는다면, num번째 순열이 속한 집합번호는
    # 1을 추가해야 한다
    if num % temp:
        nth = num // temp + 1
        # 집합번호가 정해졌기 때문에 basket에 추가한다
        basket.append(nth)
        # 무시해야 하는 집합들만큼 num을 건너뛰고 다음 자리수로 이동한다
        divide(num - (nth - 1) * temp, whole - 1, basket)
    # 그렇지 않다면, num번째 순열이 속한 집합번호는 집합의 크기로 나눈 값과 같다
    else:
        nth = num // temp
        basket.append(nth)
        divide(num - (nth - 1) * temp, whole - 1, basket)

# merge : 순열 p가 주어질 때 몇번째 순열인지 출력하는 함수
def merge(p):
    # permu : divide의 basket과 같은 역할을 한다. 즉, 집합 번호를 담는 리스트이다
    vis = [False] * (n + 1)
    permu = []
    for i in range(n - 1):
        cnt = 0
        for j in range(1, n + 1):
            if vis[j] == False:
                cnt += 1
                if j == p[i]:
                    permu.append(cnt)
                    vis[p[i]] = True
                    break
    # order : 몇번째 순열인지 저장하는 변수
    order= 0
    whole = n - 1
    # 순열의 길이를 줄여주면서 (이때까지 무시했던 집합의 갯수) * (집합의 크기)를 더해준다
    for i in permu:
        order += math.factorial(whole) * (i - 1)
        whole -= 1
    # 순열 리스트인 p가 0 base-indexed이기 때문에 최종 정답으로 1을 추가한다
    print(order + 1)

# 입력부
n = int(sys.stdin.readline())
info = list(map(int, sys.stdin.readline().split()))
ans = []

# 정답 출력
if info[0] == 1:
    divide(info[1], n, ans)
else:
    merge(info[1:])

"""
참고 https://peisea0830.tistory.com/74
"""