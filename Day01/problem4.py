# Greedy_Algorithm
# 실전문제4. 1이 될때까지

""" Q1.

- 출력되지 않음 ㅠ.ㅠ

"""

N, K = map(int, input().split()) # N, K input 값 받기

count = 0 # 조건에 해당하는 횟수를 count 하기 위한 변수 생성

while N // K == 1 and N & K ==0 : # N 나누기 K한 몫은 1, 나머지는 0이 될 때까지 돌려라.
    
    if N % K == 0: # 만약에 나머지가 0이면,
        count += 1 # count를 1만큼 올리고
        N = N // K # N은 K로 나눈 몫으로 변환

        print(count)
    
    else: # 나머지가 0이 아니면,
        N -= 1 # N 값에 1을 빼주고
        count += 1 # count는 1만큼 해준다.

        print(count)
        break


""" check!

- 해당 코드는 돌아가는 거 확인 

N, K = map(int, input().split()) # 25, 5
count = 0

if N % K == 0: 
    count += 1  
    N = N // K 

print(count) # 1
print(N) # 5

"""