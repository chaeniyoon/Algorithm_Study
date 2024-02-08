# 실전문제4. 바닥공사
"""
1. 1 x 2, 2 x 1, 2 x 2  --> 덮개를 활용해 (N x 2) 채우고자 함
2. 총 경우의 수 구하기
"""

N = int(input())

d = [0] * 1001 # N은 최대 1000

"""
d[1] = 1 # 2x1 사이즈만 가능
d[2] = 3 # (2x2 1개), (1x2 2개), (2x1 2개)
"""

def floor_construction_fibo(x):

    if x == 1:
        return 1  # 2x1 사이즈만 가능
    
    if x == 2:
        return 3  # (2x2 1개), (1x2 2개), (2x1 2개)
    
    if d[x] !=0:
        return d[x]  # 0이 아닌, 값을 부여 받았다면 해당 값 출력 !
    
    d[x] = floor_construction_fibo(x-1) + floor_construction_fibo(x-2)*2 
    """
    피보나치 수열 핵심 code!
    -> xi= x(i-1) + x(i-2)*2 라는 공식 찾음
    """
    return d[x]

print(floor_construction_fibo(N))