import sys

input = sys.stdin.readline

N, M = map(int, input().split())
num = list(map(int, input().split()))

#접두사 합 구하기
prefix_sum = [0]
sum_num = 0
for i in num:
    sum_num += i
    prefix_sum.append(sum_num)

for _ in range(M):
    start, end = map(int, input().split())
    print(prefix_sum[end] - prefix_sum[start-1])


