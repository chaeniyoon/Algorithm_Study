# 실전문제2 - 개미 전사

"""
1. 최소 한 칸 이상 떨어진 식량창고 약탈
2. 최대값 구하는 프로그램
"""

N = int(input())
food_info = list(map(int, input().split()))

d = [0] * 100 # 최대 100까지 가능

d[0] = food_info[0]  
d[1] = max(food_info[0], food_info[1]) # 서로 인접한 식량창고의 크기 비교 --> 큰 값 가져가기 위함

for i in range(2, N):
    d[i] = max(d[i-1], d[i-2] + food_info[i]) 
    """
    다이나믹 프로그래밍 핵심 code!

    1. 이전 저장소까지의 최대 음식 양 --> d[i-1]
    2. 현재 저장소 + 2번째 전의 최대 음식 --> d[i-2] + food_info[i]
    -> why? 인접하지 않게 선택하기 위한 비교
    3. max() 함수를 통한 큰 값 선택
    """

print(d[N-1])  # 마지막 저장소까지의 최대 음식 양 

 
"""
# 처음 접근 방향성

N = int(input())
food_info = list(map(int, input().split()))

stack = []

for i in range(2 ,N):
    if food_info[i-2] + food_info[i] > food_info[i+1]:
        stack.append(food_info[i-2])
        stack.append(food_info[i])
    
    else:
        stack.append(food_info[i+1])

print(stack)
"""