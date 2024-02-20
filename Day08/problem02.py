# 실전문제 3. 도시 분할 계획

"""
- N개의 집, M개의 길 -> 길은 어느 방향으로 다닐 수 있음
- 길마다 길을 유지하는 드는 유지비 존재
- 2개의 분리된 마을로 분할할 계획을 세우고 있음 -> 서로 연결 필요

-> 크루스칼 알고리즘으로 최소 신장 트리 찾은 후,
-> 간선 중 비용이 가장 큰 간선 제거하기

--> 최소 신장 트리를 찾은 후, 가장 큰 간선을 제거하는 소스코드 작성
"""

# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x) :
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x :
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b) :
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b :
        parent[b] = a
    else :
        parent[a] = b

# 노드의 개수와 간선(union 연산)의 개수 입력받기
v, e = map(int, input().split())
parent = [0] * (v + 1)

# 모든 간선을 담을 리스트와 최종 비용을 담을 변수
edges = []
result = 0

# 부모 테이블 상에서, 부모를 자기 자신으로 초기화
for i in range(1, v + 1) :
    parent[i] = i

# 모든 간선에 대한 정보를 입력받기
for _ in range(e) :
    a, b, cost = map(int, input().split())
    # 비용순으로 정렬하기 위해서, 튜플의 첫 번째 원소를 비용으로 설정
    edges.append((cost, a, b))

# 간선을 비용 순으로 정렬
edges.sort()
last = 0  # 최소 신장 트리에 포함되는 간선 중에서 가장 비용이 큰 간선

for edge in edges :
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b) :
        union_parent(parent, a, b)
        result += cost
        last = cost

print(result - last)

"""
input:
7 12
1 2 3
1 3 2
3 2 1
2 5 2
3 4 4
7 3 6
5 1 5
1 6 2
6 4 1 
6 5 3
4 5 3
6 7 4

output:
8
"""