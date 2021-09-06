# 시각
# My
n = int(input())
count = 0

for i in range(n+1):
    for j in range(60):
        for k in range(60):
            # 매 시각 안에 '3'인 포함되어 있으면 1 증가
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)




