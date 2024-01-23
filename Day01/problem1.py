# Greedy_Algorithm
# 예제 3-1.거스름돈

"""
1. 500, 100, 50, 10원 동전 무한함
2. 거스름돈 -> N원
3. N은 항상 10의 배수
"""

# sol1. 
cash = int(input("거스름돈은 얼마일까?: ")) # input 값

cash_500 = cash // 500 # 몫
cash_100 = (cash % 500) // 100 # 몫
cash_50 = ((cash % 500) % 100) // 50 # 몫
cash_10 = (((cash % 500) % 100) % 50) // 10 # 몫

total_cash = cash_500 + cash_100 + cash_50 + cash_10

# check !
# print(cash_500) 
# print(cash_100)
# print(cash_50)
# print(cash_10)

print(f'거슬러줘야 할 동전의 최소 개수는 : {total_cash}개이다.')


# sol2. 
# 함수 생성 ver
cash = int(input("거스름돈은 얼마일까?: ")) # input 값

def min_cash_count(cash):

    cash_500 = cash // 500 # 몫
    cash_100 = (cash % 500) // 100 # 몫
    cash_50 = ((cash % 500) % 100) // 50 # 몫
    cash_10 = (((cash % 500) % 100) % 50) // 10 # 몫

    total_cash = cash_500 + cash_100 + cash_50 + cash_10

    return total_cash

print(f'거슬러줘야 할 동전의 최소 개수는 : {min_cash_count(cash)}개이다.')
