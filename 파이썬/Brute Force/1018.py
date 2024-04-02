import sys
input = sys.stdin.readline

N, M = map(int, input().split())

big_chess = []
result = []
for _ in range(N):
    big_chess.append(input().strip())

#모든 경우의 시작인덱스를 전부 탐색하기 위해서
#8*8을 만들 수 있는 시작인덱스가 될 수 있는 0~(N-7)의 범위로 정한다.
for i in range(N-7):
    for j in range(M-7):
        drawB = 0 #시작지점이 'B'일 때 새로 칠해야하는 개수
        drawW = 0 #시작지점이 'W'일 때 새로 칠해야하는 개수
        #시작인덱스로부터 8*8 배열을 탐색한다.
        for a in range(i, i+8):
            for b in range(j, j+8):
                #(a+b)%2로 두 변이 겹치는 사각형의 색은 다름을 구상 가능.
                if (a + b) % 2 == 0:
                    if big_chess[a][b] != 'B':
                        drawB += 1
                    if big_chess[a][b] != 'W':
                        drawW += 1
                else:
                    if big_chess[a][b] != 'W':
                        drawB += 1
                    if big_chess[a][b] != 'B':
                        drawW += 1
        result.append(drawB)
        result.append(drawW)

print(min(result))

