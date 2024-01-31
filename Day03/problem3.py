# 실전문제 4.
# 두 배열의 원소 교체

"""
문제)
- N개의 원소로 구성된 배열 (A,B)
- K번의 바꿔치기 연산을 수행하여 A의 모든 원소의 합이 최대가 되도록
"""

# 1. input 값 받기
N, K = map(int, input().split())
A_B_list = [list(map(int, input().split())) for _ in range(2)] # 항상 A,B 2가지 존재하기에 range(2) -> 2차원 array 생성!

# 2. for 문으로 A, B 를 각각 오름차순 내림차순으로 정렬하기
"""
- A를 오름차순으로 정렬한 후, K만큼 for 문을 돌려서 앞에 K개의 A의 요소를
- 내림차순으로 정렬한 B의 K개의 요소로 바꿔주기 위함

"""
for i in range(1,N):
    for j in range(i, 0, -1):

        # A의 경우, 오름차순으로 정렬
        if A_B_list[0][j] < A_B_list[0][j-1]: # 오름차순 배열이기에 뒤에 위치한 숫자가 크면, 두 숫자의 위치를 바꿔야 함 ! 
            A_B_list[0][j], A_B_list[0][j-1] = A_B_list[0][j-1], A_B_list[0][j]
        
        # B의 경우, 내림차순으로 정렬
        if A_B_list[1][j] > A_B_list[1][j-1]: # 내림차순 배열이기에 뒤에 위치한 숫자가 크면, 두 숫자의 위치를 바꿔야 함 ! 
            A_B_list[1][j], A_B_list[1][j-1] = A_B_list[1][j-1], A_B_list[1][j]

# 3. for 문으로 K만큼 순회하면서, 해당하는 위치의 값을 바꿔줌
for K_data in range(K):
    A_B_list[0][K_data] = A_B_list[1][K_data]
    # print(A_B_list)

# 4. A의 list 요소의 합을 구해주기
max_sum = 0
for A in A_B_list[0]:
    max_sum += A

# 5. 최종 print!
print(max_sum)