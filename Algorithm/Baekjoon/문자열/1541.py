# 1541
n = input().split('-')
# print(n)
result = 0
for i in n[0].split('+'):
    result += int(i)

for i in n[1:]:
    for j in i.split('+'):
        result -= int(j)

print(result)


"""
- 가장 처음 나오는 - 이전까지는 모두 더할 수 밖에 없으며 그 이후에는 모두 빼주면 된다.
- 예를 들어 55-50+40의 최소값을 만드려면 55-(50+40)을 만들어줘야 하는데 이는 결국 55-50-40과 같은 말이다.
- 입력을 받을 때 -를 구분자로 하여 입력을 받고 리스트의 첫 번째 요소(마이너스가 나오기 전까지의 원소)들은 모두 더해준다. 
- 그런 다음 나머지 요소들을 모두 빼주면 되는데 이때 ['20', '30+40']과 같이 +기호가 포함된 원소들이 존재할 수 있으므로 
+를 구분자로 하여 다시금 분리해주게 되면 ['20', '30', '40']과 같이 분리되게 된다. 이제 이 원소들을 모두 빼주면 된다. 
"""