# 실전문제5 - 효율적인 화페 구성

"""
1. N가지 종류의 화페, M원이 되도록 구성 필요
2. 최소한의 화페 개수 출력
"""

"""
-> 점화식 활용 x
"""

N, M = map(int, input().split()) 

money_type = []  # 화폐 종류를 받을 새로운 리스트 생성
for i in range(1, N+1):
    money_type.append(int(input()))

# print(money_type) # [3,5,7]

money_type.sort(reverse= True) # [7,5,3]
"""
1. 내림차순 정렬
-> 최소한의 화페 개수를 출력하기 위해, 추후 리스트를 큰 값부터 돌리기 위함
"""

count = 0  # 최소한의 화페 개수를 출력하기 위한 변수 생성
for i in money_type:
    count = count + M // i  # 해당 몫은 count에 더해주고,
    M = M % i  # 나머지는, M으로 다시 부여

print(count)

