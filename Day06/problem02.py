# 실전문제 4. 미로탈출

"""
- N X M 크기의 직사각형 형태의 미로에 갇힘
- 동빈이의 현재 위치는 (1,1) 미로의 출구 (N,M), 한 칸씩 이동 가능
- 괴물이 있는 부분 0, 없는 부분 1
- 탈출하기 위한 최소 칸의 개수
- 칸을 셀 때는 시작 칸과 마지막 칸 모두 포함한 후 계산
"""

"""
BFS를 활용해야 하는 포인트?
-> '최소 칸' --> BFS는 시작 지점에서 가까운 노드부터 차례대로 그래프의 모든 노드를 탐색하기 때문
"""

"""
- 문제 풀이 확인했음
"""

from collections import deque

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int,input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS 소스 코드 구현
def bfs(x,y):
    # queue 구현을 위해 deque 라이브러리 사용
    queue = deque()
    queue.append((x,y))

    # 큐가 빌 때까지 반복
    while queue:
           x, y = queue.popleft()  # pop()위 반대 --> 인덱스 제일 앞의 요소 삭제
           for i in range(4):
                """
                현재 위치(x,y)에서 네 방향으로의 위치 확인
                """
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or ny < 0 or nx >= n or ny >= m:
                     continue  # 공간을 벗어나면 무시
                if graph[nx][ny] == 0:
                     continue  # 벽인 경우에도 무시
                if graph[nx][ny] == 1:
                     """
                     공간을 벗어나지 않고, 괴물이 없는 경우 + 처음 방문하는 경우
                     -> 이전 칸으로부터 1 증가시킨 후, 해당 위치를 queue에 append!
                     """
                     graph[nx][ny] = graph[x][y] + 1  #  처음 방문하는 경우에 최단 거리 기록
                     queue.append((nx,ny))

    return graph[n-1][m-1]  # 최단거리 반환

print(bfs(0,0))
print(graph)

"""
[[3, 0, 5, 0, 7, 0], 
[2, 3, 4, 5, 6, 7], 
[0, 0, 0, 0, 0, 8], 
[14, 13, 12, 11, 10, 9], 
[15, 14, 13, 12, 11, 10]]
"""
