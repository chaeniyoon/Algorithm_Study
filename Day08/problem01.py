# 실전문제 2. 팀 결성

"""
- 학교에서 학생들이게 0 ~ n번까지의 번호 부여
- 모든 학생이 서로 다른 팀으로 구분 --> 총 n+1개의 팀 존재
- 팀 합치기(두 팀 합치기) / 같은 팀 여부 확인(같은 팀에 합치는지)

--> 서로소 관련 문제 !
--> 앞의 예제문제와 비슷
"""

# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드가 아니면 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x

# 두 원소가 속한 집합 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())
parent = [0] * (n + 1)  # 부모 테이블 초기화

# 부모 테이블 상에서, 부모를 자기 자신으로 초기화
for i in range(0, n + 1) :
   parent[i] = i

# 각 연산을 하나씩 확인
for i in range(m) :
    oper, a, b = map(int, input().split())
   # 합집합(union) 연산인 경우,
    if oper == 0 :
     union_parent(parent, a, b)
    # 찾기(find) 연산인 경우,
    elif oper == 1 :
        if find_parent(parent, a) == find_parent(parent, b) :
            print('YES')
    else :
      print('NO')

"""
input:
7 8
0 1 3
1 1 7
0 7 6
1 7 1
0 3 7
0 4 2
0 1 1
1 1 1

output:
NO
NO
YES

"""