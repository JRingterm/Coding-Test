import sys
input = sys.stdin.readline

#=====sort() 함수 쓴 버전=====
# N = int(input())
# n_list = []

# for _ in range(N):
#     n_list.append(int(input()))
# n_list.sort()

# #한줄에 하나씩 출력하기 위해 *로 Unpacking한 데이터로 전달한다.
# print(*n_list, sep='\n') 

#=====sort() 함수 안 쓴 버전=====

N = int(input())
n_list = []

for _ in range(N):
    n_list.append(int(input()))

for i in range(N):
    for j in range(0, N-i-1):
        if n_list[j] > n_list[j+1]:
            n_list[j], n_list[j+1] = n_list[j+1], n_list[j] #위치 변환
            
print(*n_list, sep='\n')

