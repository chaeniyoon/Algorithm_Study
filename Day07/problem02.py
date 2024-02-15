# 실전문제 9-5. 전보

"""
- N개의 도시 존재
- 보내고자 하는 메시지 -> 다른 도시로 전보를 보내서 해당 메시지 전송 가능

- 이때, X -> Y로 보내려면 향하는 통로가 설치되어 있어야 함
- X -> Y는 있는데, Y -> X가 없으면 보낼 수 없다는 것을 의미!
- 또한, 통로를 거쳐 메시지를 보낼때는 일정 시간 소요

- C라는 도시에서 위급 상황 발생 --> 최대한 많은 도시로 메시지를 보내고자 함
- C에서 출발하여 각 도시 사이에 설치된 통로를 거쳐, 최대한 많이 퍼져나갈 것

--> 이때, C에서 보낸 메시지를 받게 되는 도시의 개수는 총 몇 개? 총 몇 시간?
"""

"""
1. 한 도시에서 -> 다른 도시까지의 최단 거리
--> 따라서 다익스트라 알고리즘 활용 !!!

2. N과 M의 범위가 충분히 크기에
--> 우선순위 큐를 이용하여 작성 필요
"""

import heapq
import sys

input = sys.stdin.readline
INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

# 노드의 개수, 간선의 개수, 시작 노드를 입력받기
n, m, start = map(int, input().split())

# 각노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] for i in range(n+1)]

# 최단 거리 테이블을 모두 무한으로초기화
distance = [INF] * (n+1)

# 모든 간선 정보를 입력받기
for _ in range(m):
    x, y, z = map(int, input().split())  
    """  
    """
    # x번 노드에서 y번 노드로 가는 비용이 z라는 의미
    graph[x].append((y,z))

# 함수 정의!
def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    
    while q: # 큐가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적 있다면 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접 노드 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

# 다익스트라 알고리즘을 수행               
dijkstra(start)

# 도달할 수 있는 노드의 개수
count = 0

# 도달할 수 있는 노드 중에서, 가장 멀리 있는 노드와의 최단 거리
max_distance = 0

for d in distance:
    # 도달할 수 없는 경우
    if d != INF:
        count += 1
        max_distance = max(max_distance, d)

# 시작 노드는 제외해야 하므로 count -1을 출력
print(count - 1, max_distance)

"""
input:
3 2 1
1 2 4
1 3 2

output:
2 4
"""