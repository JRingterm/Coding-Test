import sys

input = sys.stdin.readline

N = int(input())

stairs = [0] * 301   #계단의 최대 갯수만큼 배열 초기화
dp = [0] * 301   #인덱스는 현재 계단 위치, 값은 그 위치에 있을 때의 최대값

for i in range(1, N+1):
    stairs[i] = int(input())

# 각 계단을 밟았을 때의 점수 최댓값
dp[1] = stairs[1]
dp[2] = stairs[1] + stairs[2]
dp[3] = max(stairs[1] + stairs[3], stairs[2] + stairs[3])
# 점화식 dp(n) = max(직전 칸에서 올라온 경우의 최대값, 전전 칸에서 올라온 경우의 최댓값)

# 직전 칸에서 올라온 경우, 전전칸은 밟을 수 없기 때문에, 전전전칸의 dp를 더해야 한다.
# dp(n-3) + stairs[n] + stairs[n-1]

# 전전 칸에서 올라온 경우, 전전칸의 dp와 올라온 현재 칸의 점수를 더해주면 된다.
# dp[i-2] + stairs[n]

for i in range(4,N+1):
    dp[i] = max(dp[i-3] + stairs[i] + stairs[i-1], dp[i-2] + stairs[i])

print(dp[N])
