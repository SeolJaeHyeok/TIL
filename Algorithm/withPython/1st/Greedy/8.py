# ATM, 11399
n = int(input())
p = list(map(int, input().split()))
p.sort()
result = 0
sum_value = 0
for i in range(len(p)):
    sum_value = sum_value + p[i]
    result += sum_value

print(result)

"""
접근 방법
- 걸리는 시간을 오름차순으로 정렬하여 차례대로 더하면 걸린 시간의 합계가 최소가 된다
- 각 인덱스까지 걸리는 시간을 구하고(sum_value) 해당 값을 최종 결과(result)에 더해준다. 
"""
