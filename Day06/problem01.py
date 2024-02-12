# 실전문제3. 음료수 얼려 먹기
"""
문제)
- N X M 크기의 얼음 틀 존재
- 구멍이 뚫려 있는 부분은 0, 칸막이가 존재하는 부분은 1
- 얼음 틀의 모양이 주어졌을 때, 생성되는 총 아이스크림의 개수
"""
"""
- 감이 안와서, 문제 해설 보고 풀었음
- pythonTutor 보면서 이해하려고 노력중...
"""

# N, M을 공백으로 구분하여 입력받기
n, m = map(int, input().split())

# 2차원 리스트의 맵 정보 입력받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# DFS로 특정한 노드를 방문한 뒤에 연결된 모드 노드들도 방문
def dfs(x,y):
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    
    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0:
        # 해당 노드 방문 처리
        graph[x][y] = 1
        # 상, 하, 좌, 우의 위치도 모두 재귀적으로 호출
        dfs(x-1, y) # 상
        dfs(x+1, y) # 하
        dfs(x, y-1) # 좌
        dfs(x, y+1) # 우
        return True
    return False

# 모든 노드(위치)에 대하여 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        # 현재 위치에서 DFS 수행
        """
        아래의 조건이, result와 연관이 있는건지 이해 x
        -> 위의 방문처리를 하는 과정과 연관 + ..?
        """
        if dfs(i, j) == True:
            result += 1

print(result)


