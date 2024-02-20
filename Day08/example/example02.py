# 10-2. 경로 압축 기법 소스코드

"""
경로 압축 기법?
- 재귀적으로 후출한 뒤, 부모 테이블 값을 갱신하는 기법
- 결과적을, 경로 압축 기법을 이용하면, 루트 노드에 더욱 빠르게 접근할 수 있다는 점
"""

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]