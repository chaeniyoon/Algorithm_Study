# 실전문제3 - 떡볶이 떡 만들기

"""
- 이진 탐색 적용...X
"""

N, M = list(map(int, input().split()))
N_list = list(map(int, input().split()))


result = []

for i in range(max(N_list), 0 , -1):
    """
    1. range를 역순으로 돌면서 --> 즉, 떡 길이의 data 중 가장 긴 길이부터 1씩 작아지면서 순차적으로 비교
    2. 기준이 되는 길이보다 긴 길이가 없으면 --> count 하지 않고
    3. 기준이 되는 길이보다 긴 길이가 있다면 --> count를 해줌
    4. 이때, count한 값이 주어진 M과 같다면 그 값을 return 해줌
    5. 그런데, 6cm를 남기는데 있어 15,14,13의 길이를 자를 때 모두 해당하는 case를 해결하기 위해서
    6. 최대값을 추출 -->  15,14,13을 result라는 새로운 리스트에 append 하고 이때의 0의 인덱스 값을 print!
    """
    count = 0
    for j in N_list:
        if i >= j:
            count = count

        else:
            count += j - i
            if count == M:
                result.append(i)

print(result[0]) # 최대값을 구하기 위해 인덱스 0의 요소를 받아옴