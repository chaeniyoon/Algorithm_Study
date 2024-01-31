# 실전문제 3.
# 성적이 낮은 순서로 학생 출력하기

"""
문제)
- 첫 번째 줄에 학생의 수 N이 입력
- 두 번째 줄부터는 학생의 이름 문자열 A, 학생의 성적 정수 B
- 성적이 낮은 순서대로 이름 출력
"""

# 1. input 받을 학생-성적 수
N = int(input())

# 2. input 받을 학생 - 성적 data
name_score_list = [list(input().split()) for _ in range(N)]
# print(name_score_list) # 출력 예시 : [['홍길동', '34'], ['이순신', '55']]

# 3. for문
"""
- name_score_list의 두번째 인덱스에 해당하는 성적 -> name_score_list[j][1] 을 int로 자료형 변환하여 크기 비교
- 오름차순 배열에 맞게 if 문 정리
"""
for i in range(1, N): # 1부터 ~ N-1 까지 ex. N=5 이면, 1 ~ 4
    for j in range(i, 0, -1): # j에 4,3,2,1 순으로 들어감
        if int(name_score_list[j][1]) < int(name_score_list[j-1][1]): # 오름차순 배열이기에 앞에 위치한 숫자가 크면, 두 숫자의 위치를 바꿔야 함 ! 
            name_score_list[j], name_score_list[j-1] = name_score_list[j-1], name_score_list[j] # array 위치 바뀜
        else:
            break

# 4. print
"""
- name에 해당하는 요소만 추출 -> name_data[0]
"""
for name_data in name_score_list:
    print(name_data[0], end = ' ')