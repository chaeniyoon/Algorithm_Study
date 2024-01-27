# CHAPTER 04. 구현
# 실전문제 3. 게임 개발

"""
KEY POINT!
- 문제 이해 못함 ㅜ.ㅜ
1. 이동할 size 값 받기 --> 
2. 위치와 바라보고 있는 시점 값 받기 --> 
3. 해당 맵 구성하기 --> 
"""

# 1. 이동할 직사각형 값 받기
N, M = map(int, input().split())

# 2. x,y 좌표와 방향(동, 서, 남, 북) 값 받기
x, y, direction = map(int, input().split())

# 3. 해당 맵 구성하기

map_list = []

for date in range(N):
    """
    check!
    - 입력 값을 받을 리스트 생성 -> map_list
    - N개의 리스트 안의 리스트를 구성해야하기에 rnage(N) 만큼 for문 돌리기
    - append 함수를 통한 input 값 map_list에 추가
    """
    map_list.append(list(map(int, input().split())))

# 4. 방문하는 수
count = 0

"""
check!
- 아마, 반복문을 돌면서 만족하는 조건에 값이 해당하면 count +=1 을 해주는 형식일거라고 예상
"""