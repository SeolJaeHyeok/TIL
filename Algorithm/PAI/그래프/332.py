# Reconstruct Itinerary
from collections import defaultdict

def findItinerary(tickets: list):
    graph = defaultdict(list)
    # 사전 순으로 정리
    for a, b in sorted(tickets):
        graph[a].append(b)

    answer = []
    def dfs(a):
        while graph[a]:
            # 첫 번째 값을 호출하여 사전 순으로 방문
            dfs(graph[a].pop(0))
        answer.append(a)

    dfs('JFK')
    # 다시 뒤집어서 어휘순 결과로 반환
    return answer[::-1]

print(findItinerary([["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]))
print(findItinerary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]))