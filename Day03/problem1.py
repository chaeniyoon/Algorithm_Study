# 실전문제 2.
# 위에서 아래로

"""
문제)
- 수를 큰 수부터 작은 수의 순서로 정렬
-> 즉, 수열을 내림차순으로 정렬하는 프로그램 만들기

1. 첫째 줄에 수열에 속해 있는 수의 개수 N (1 <= N <= 500)
2. 둘째 줄부터, N+1번째 줄까지 N개의 수 입력 
"""

# 1. input

N = int(input())  # 몇 개 받을거니?
# num_array = [] # 어떤 숫자로 받을거니?

num_array = [list(map(int,input())) for _ in range(N)]
print(num_array)

"""
input 받을 때, append를 쓰지 않는다면?..?
num_array = [list(map(int, input())) for _ in range(N)] 

-> 2차원 배열로 받아서, N x 1 형식으로 받은 다음에
-> 해당 인덱스의 요소 값들을 배열하는 방식으로 풀려고 했으나
5
17
15
64
21
2
[[1, 7], [1, 5], [6, 4], [2, 1], [2]] 이렇게 출력..
"""

"""
for num in range(N): # 해당 num_list input 값 받기
    num_array.append(int(input()))

# print(num_array)

for i in range(1, N): # 1부터 ~ N-1 까지 ex. N=5 이면, 1 ~ 4
    for j in range(i, 0, -1): # j에 4,3,2,1 순으로 들어감
        if num_array[j] > num_array[j-1]: # 내림차순 배열이기에 뒤에 위치한 숫자가 크면, 두 숫자의 위치를 바꿔야 함 ! 
            num_array[j], num_array[j-1] = num_array[j-1], num_array[j]
        else:
            break

for result_data in num_array:
    print(result_data, end = ' ')
"""