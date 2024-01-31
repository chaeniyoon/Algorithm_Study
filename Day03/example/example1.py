# example 1.
# 선택 정렬 소스코드

"""
선택 정렬?
- 가장 작은 데이터를 앞으로 보내는 과정을 N-1번 반복하면
-> 정렬 완료 !
"""

array = [7,5,9,0,3,1,6,2,4,8]

for i in range(len(array)): # array의 길이만큼 돌면서,
    min_index = i # 가장 작은 인덱스
    for j in range(i+1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    
    array[i], array[min_index] = array[min_index], array[i] # 스와프

print(array)

# 스와프 소스코드

"""
스와프?
- 두 변수의 위치를 변경하는 작업을 의미
-> 명시적으로 임시 저장용 변수를 만들어, 두 원소의 값을 변경
"""

# 0 인덱스와 1 인덱스 원소 교체하기
array = [3, 5]
array[0], array[1] = array[1], array[0]

print(array)