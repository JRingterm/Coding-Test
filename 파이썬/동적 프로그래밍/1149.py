import sys
input = sys.stdin.readline

N = int(input())
# cost = []
# for i in range(N):
#     cost.append(input().strip().split())
cost = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * 3 for _ in range(N)] #비용 계산을 위한 배열
dp[0] = cost[0]

for i in range(1,N):
    #현재 열을 제외한 i-1행의 열들 중 최솟값 + 현재 칸 비용
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + cost[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + cost[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + cost[i][2]

print(min(dp[N-1]))

