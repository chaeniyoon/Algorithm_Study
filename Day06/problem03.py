# 백준
# 10451번. 순열사이클

"""
N개의 정수로 이루어진 순열 주어졌을 때, 순열 사이클의 개수는?
"""

"""
- 문제풀이 참고
"""

"""
ex)
1 2 3 4 5 6 7 8 --> 즉, 인덱스
3 2 7 8 1 4 5 6 --> 즉, input data

(cnt: 1회)
1. 1부터 시작해서 arr[1]이 가르키는 3을 인덱스로 하는 곳으로 넘어감
2. arr[3]이 가르키는 7을 인덱스로 하는 곳으로 넘어감
3. arr[7]이 가르키는 5를 인덱스로 하는 곳으로 넘어감
4. arr[5]가 가르키는 1은 이미 한 번 지나왔던 곳

--> 즉 사이클이 1 - 3 - 7 - 5 이렇게 생겼고, 이때 cnt +1 --> cnt = 1

(cnt: 2회)
1. 다음 2로 넘어감
2. arr[2]가 가르키는 2는 인덱스 2

--> 즉 사이클은 2이며, 이때 cnt +1 --> cnt = 2

(cnt: 3회)
1. 3 넘어가고 4로 이동
2. arr[4]가 가르키는 8을 인덱스로 하는 곳으로 넘어감
3. arr[8]이 가르키는 6을 인덱스로 하는 곳으로 넘어감
4. arrp6]이 가르키는 4는 한 번 지나왔던 곳

--> 즉 사이클이 4 - 8 - 6 이렇게 생겼고, 이때 cnt +1 --> cnt = 3

더이상 순회할 사이클은 없기에, 답은 cnt = 3
"""

def dfs(v):
    visited[v] = 1  # 1로 바꿔주고,
    next = arr[v]
    if visited[next] == 0:
        dfs(next)
    return


T = int(input())  # 테스트 케이스 수

for tc in range(1, T+1):
    cnt = 0  # 최종 답안 !

    N = int(input())  # 받고자 하는 arr의 num 수
    visited = [0] * (N + 1)  # 방문했을 때 체크를 해주기 위한 new 리스트 생성
    arr = list(map(int, input().split()))

    arr.insert(0, 0)  # 0번째에 0을 추가 --> 인덱스 번호와 위치를 동일시 하기 위함
    for i in range(1, N + 1):
        if visited[i] == 0:
            dfs(i)
            # print(visited) # check !
            cnt += 1

    print(cnt)