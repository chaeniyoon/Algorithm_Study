# 5-3. 재귀함수
"""
재귀함수란? 
- 자기 자신을 다시 호출하는 함수를 의미
"""

def recursive_function():
    print('재귀함수를 호출합니다.')
    recursive_function()

recursive_function()