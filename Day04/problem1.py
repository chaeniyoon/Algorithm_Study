# 실전문제2 - 부품찾기

"""
1. M_list에 있는 부품 번호가 N_list에 존재하는 지 단순 in을 활용해서 풀기
"""
# input 값

N = int(input()) # 가게에 있는 부품 수
N_list = list(map(int, input().split())) # 가게의 총 부품 번호
            
M = int(input()) # 부품 확인 요청 개수
M_list = list(map(int, input().split())) # 요청한 부품 번호

# print !

for i in M_list:
    if i in N_list:
        print("yes", end= ' ')
    
    else: 
        print("no", end= ' ')