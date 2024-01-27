# CHAPTER 04. 구현
# 예제 4-2. 시각

"""
처음에는?
-> 경우의 수를 계산해서 적용하려고 함
-> 예를 들어, input 값이 3이면 ~ 3시 59분 59초까지 인거고 
-> 3시 ~ 3시 59분 59초는 무조건 3600가지의 경우의 수 존재 ... 
-> 근데 이렇게 하기에는 계산을 각각 해야해서 식을 만들어야 하는 번거로움 존재
: for문을 활용해서 풀려고 방향성 바꿈...!
"""

"""
KEY POINT!
1. N시까지의 값을 input으로 받기 -> hour
2. for in range()문을 활용하여 3이 하나라도 포함이 되는지 포함되지 않은지 파악하기
3. 시, 분, 초에 맞는 range() 설정을 통한 for문 반복

"""

# 1. input 값 받기 N시에 해당하는 hour
hour = int(input())

# 2. for 문을 돌리면서, 3이 하나라도 포함되어 있으면 count 해주는 count 변수 생성
count = 0

for hour_data in range(hour+1):
    """
    check!
    - 이때, hour에 1을 더하는 이유는? 0시 부터 시작하기 때문에
    """
    for minute_data in range(60):
        """
        check!
        - 이때, range(60)을 하는 이유는? 0부터 59까지라서
        """
        for second_data in range(60):
            """
            check!
            - 이때, range(60)을 하는 이유는? 0부터 59까지라서
            """
            if '3' in str(second_data) or '3' in str(minute_data) or '3' in str(hour_data):
                """
                check!
                - 처음에, if 3 in second_data... 이렇게 code를 구성하니 TypeError 발생
                - 이는 정수, 실수 등과 같은 자료형은 순회하면서 정의할 수 있는 자료형이 아니기 때문 --> 즉, str 문자열과 같이 순회할 수 있는 자료형으로 변환
                """
                count += 1 # 3. 1을 더해줌

# 4.값 출력
print(count)