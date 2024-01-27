 # CHAPTER 04. 구현
# 예제 4-1. 상하좌우

"""
KEY POINT!
1. 정사각형 사이즈 값 받기 -> move_size
2. 이동하는 방향 값 받기 -> move_routine
3. 최종적으로 도착할 지점의 좌표를 출력하는 프로그램 
"""

# 1. input 값 받기(정사각형 사이즈, 이동 방향)
move_size = int(input('정사각형 공간의 크기를 정해주세요: '))
move_routine = map(str, input().split())

x = 1
y = 1

for data in move_routine:
    if data == 'R':
        """
        check!
        - R: 오른쪽으로 1칸 이동
        -> y의 좌표가 이미 move_size만큼 이동했다면, move_size 반영하기 위함
        """
        if y < move_size:
            y += 1
        else:
            y = move_size
    
    elif data =='L':
        """
        check!
        - L: 왼쪽으로 1칸 이동
        -> y의 좌표가 1이라면, 1에 있기 위함
        """
        if y > 1:
            y -= 1
        else:
            y = 1

    elif data =='U':
        """
        check!
        - U: 위로 1칸 이동
        -> x의 좌표가 1이라면, 1에 있기 위함
        """
        if x > 1:
            x -= 1
        else:
            x = 1

    else:
        """
        check!
        - D: 아래로 1칸 이동
        -> x의 좌표가 이미 move_size만큼 이동했다면, move_size 반영하기 위함
        """
        if x < move_size:
            x += 1
        else:
            x = move_size

print(x,y)


