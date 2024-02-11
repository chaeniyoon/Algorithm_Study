# 5-2. 큐 예제
"""
deque는 스택과 큐의 장점을 모두 채택한 것 -> 데이터를 넣고, 빼는 속도가 빠름
-> 코테에서도 사용 가능한 라이브러리
"""
from collections import deque 

# 큐(queue) 구현을 위해, deque 라이브러리 사용
queue = deque()

# 삽입 5 -> 2 -> 3 -> 7 삭제() 삽입 1 -> 4 삭제()
queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)

queue.popleft()  # 5 삭제

queue.append(1)
queue.append(4)
queue.popleft()  # 2 삭제

print(queue)  # 먼저 들어온 순서대로 출력, 출력결과: deque([3, 7, 1, 4])
print(list(queue))  # list를 사용함으로써, 출력결과: [3, 7, 1, 4]

queue.reverse()  # 다음 출력을 위해 역순으로 바꾸기
print(queue)  # 나중에 들어온 원소부터 출력
