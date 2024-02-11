# 5-1. 스택 예제
"""
append, pop 메서드의 경우, 별도의 라이브러리 필요없음
stack은 선입후출, 후입선출 구조

- append -> 데이터 추가
- pop -> 마지막 데이터 삭제
- pop(a) -> a에 위치한 데이터 삭제
"""

stack = []

# 삽입 5 -> 2 -> 3 -> 7 삭제() 삽입 1 -> 4 삭제()
stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)

stack.pop()  # 7 삭제

stack.append(1)
stack.append(4)

stack.pop()  # 4 삭제

print(stack)  # 최하단 원소부터 출력
print(stack[::-1])  # 최상단 원소부터 출력
