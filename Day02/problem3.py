# CHAPTER 04. 구현
# 실전문제 - 왕실의 나이트

"""
KEY POINT!
1. 위치데이터 받기 -> garden_data
2. 가능한 이동 경우 리스트로 만들기 -> move_list
3. 경우의 수를 세는 변수 생성 -> count
4. for 문으로 move_list를 돌면서 해당 값과 input 값을 더했을 때 1 이상 8 이하인지 파악 후 해당하면 count +1
"""

# 1. input으로 정원의 위치 데이터 받기
garden_data = str(input())

# 2. 가능한 이동 case를 파악한 후 리스트로 생성 -> move_list
move_list = [(2,1), (2,-1), (-2,1), (-2,-1), (1,2), (-1,2), (1,-2), (-1,-2)]

# 3. 이동할 수 있는 경우의 수를 count할 변수 생성 -> count
count = 0

# 4. for 문
for move in move_list:
    if int(move[0]) + int(ord(garden_data[0]))-96 >= 1 and int(move[0]) + int(ord(garden_data[0]))-96 <= 8 and int(move[1]) + int(garden_data[1]) >= 1 and int(move[1]) + int(garden_data[1]) <= 8:
        """
        check!
        - input 값과 해당 case의 값을 더했을 때 무조건 1이상이어야 함 -> why? 최소 (1,1)에서 시작하기에
        - input 값과 해당 case의 값을 더했을 때 무조건 8이하이어야 함 -> why? 최소 (8,8)에서 끝나기에
        - ord 함수를 활용한 아스키코드를 숫자로 반환 -> 이때, 알파벳 a가 97이기에 96을 빼줌 why? a가 곧 1이고, 1을 만들기 위해서
        - garden_data, move 모두 string 문자열이기에 int type으로 변환 필요
        """
        count += 1

# 5. 출력       
print(count)