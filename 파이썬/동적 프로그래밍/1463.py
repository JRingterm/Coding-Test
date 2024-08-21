import sys

input =sys.stdin.readline

N = int(input())

#DP 테이블 초기화
d = [0] * 1000001

#DP 진행(bottom-up)
for i in range(2, N+1):
    #현재의 수에서 1을 빼는 경우 -> 계산 횟수 +1
    d[i] = d[i-1] + 1   #이전 결과를 다음 결과에 이용.

    #현재의 수가 2로 나누어 떨어지는 경우
    if i % 2 == 0:
        #min(현재 수에서 1을 빼는 경우의 계산 횟수, 현재 수를 2로 나누었을 경우에 나오는 수의 계산 횟수 +1)
        d[i] = min(d[i], d[i//2] + 1) 

    if i % 3 == 0:
        #min(현재 수에서 1을 빼는 경우의 계산 횟수, 현재 수를 3으로 나누었을 경우에 나오는 수의 계산 횟수 +1)
        d[i] = min(d[i], d[i//3] + 1) 

print(d[N])