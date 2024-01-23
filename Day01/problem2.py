# Greedy_Algorithm
# 실전문제2. 큰 수의 법칙

""" check!

1. M과 K의 관계
- 2번째로 큰 값의 수는 M //(K+1) 한 만큼 개수
- 가장 큰 값의 수는 M -(M//(K+1)) 한 만큼 개수

"""

""" how to solve?

1. map(적용할 함수, 반복 가능한 자료형)
2. N개 만큼 어떻게 받아올건지 --> 가장 많이 고민 
3. .remove() 활용함으로써 일치하는 항목 하나만 삭제
- why? 가장 큰 값과 두번째로 큰 값이 같을 수도 있기에, 그 case 반영하기 위함

"""

N, M, K = map(int, input().split()) # N, M, K input 값 받기

N_list = list(map(int, input().split()))[:N] # N수 만큼 input 값 받기

""" Q1. 

N_list = []

for i in range(N):
    N_list.append(input(N)) --> 시도해봤는데, 다르게 나옴 ㅠ.ㅠ

print(N_list)

"""

first_max_data = max(N_list) # 가장 큰 값

""" Q2.

- for 문을 돌려서, 해당 리스트를 돌고
- if 문으로 first_max_data == i 랑 같으면, 제거한다 ..! 
-> 이때의 문제점, 가장 큰 값과 두번째로 큰 값이 같다는 것을 반영 못한다?

"""

N_list.remove(first_max_data) # 해당 한 개의 데이터 삭제
second_max_data = max(N_list) # 두번째로 큰 값

first_exp = first_max_data * (M -(M//(K+1)))
second_exp = second_max_data * (M //(K+1))

result = first_exp + second_exp

print(result)