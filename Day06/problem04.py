# 백준
# 1389. 케빈 베이컨위 6단계 법칙

"""
사람들의 연결 정보를 확인해서, 연결 경로가 최소인 사람을 찾는 문제
-> 최소 --> BFS 활용 필요
"""

"""
- 문제풀이 참고
- 계속 풀어보면서, 이해가 필요할 거 같음
"""

from collections import deque

N, M = map(int, input().split())

arr = [[] for _ in range(N+1)]
for i in range(M):
    u, v = map(int, input().split())
    """
    양방향 노드로 arr를 생성해야 함
    """
    arr[u].append(v)
    arr[v].append(u)

def bfs(start):
    visited = [-1] * (N + 1)

    q = deque()
    q.append(start)
    visited[start] = 0
    """
    첫 번째 위치만, 거리 계산을 위해 0 으로 초기화
    """

    while q:  # 모든 연결 가능한 사람까지의 케빈 베이컨 수 구하기
        node = q.popleft()  

        for next_node in arr[node]:
            if visited[next_node] == -1:
                """
                - 방문하지 않은 곳 탐색 --> 방문하지 않은 곳은 곧 '-1'
                - 다음 노드 탐색을 위해 노드에 1 더해줌
                """
                visited[next_node] = visited[node] + 1
                q.append(next_node)
    total = sum(visited)
    """
    최소 길이를 더한 케빈 베이컨 수를 구하는 것이 목표
    -> visitied에 최소 거리가 저장되어 있기에 sum 한 값은 곧, 케빈 베이컨 수 
    """
    return total

min_total = float("INF")  # 무한대의 값으로 초기화 --> 최소의 값을 구하기 위함
result = 0
for i in range(1, N+1):

    total = bfs(i)
    if total < min_total:
        min_total = total
        result = i  # 최소의 케빈 베이컨 수가 아닌, 최소의 케빈 베이컨 수를 가진 사람을 찾는 것

print(result)