# Greedy_Algorithm
# 실전문제3. 숫자 카드 게임

""" check!

1. 문제 이해
- 먼저 뽑고자 하는 행 선택
- 그다음 선택된 행에 포함된 카드들 중 낮은 카드 선택
- 따라서, 이후에 해당 행에서 가장 숫자가 낮은 카드를 뽑을 것을 고려하여 뽑아라

-> why? 이 결론이 '각 행마다 가장 작은 수를 찾은 뒤에 그 수 중에서 가장 큰 수'를 찾는 거지...?

"""

N, M = map(int, input().split()) # N, M input 값 받기

N_list = [] # 안에 넣을 데이터 값 받기

""" Q1.

이때, N,M 행렬만큼 데이터 수를 받는 조건을 부여하고 싶은데 관련 코드를 구현 못함 ㅜ.ㅜ

"""

for i in range(N):
    
    N_list.append(list(map(int, input().split())))

min_list = []


for j in N_list:
    a = min(j)
    min_list.append(a) # min_list에 각 리스트마다 작은 값들을 할당

result = max(min_list) # min_list에서 가장 큰 값을 result에 저장
print(result)


""" Q2. 

# 처음 이해한 방향 
-> 가장 작은 값을 가지고 있는 리스트를 제거한 후, 나머지 리스트에서 가장 작은 값을 구해라

N_list.remove(min(N_list))
print(min(min(N_list)))

"""

# result = min_list.remove(min(min_list))
# result2 = min(result)
# print(result2)