import sys
input = sys.stdin.readline

N, M = map(int, input().split())

floor = []
for _ in range(N):
    floor.append(input().strip())

count = 0

for i in range(N):
    w_visited = False
    for j in range(M):
        if floor[i][j] == '-' and w_visited == False:
            w_visited = True
            count += 1
        elif floor[i][j] == '|':
            w_visited = False

for i in range(M):
    l_visited = False
    for j in range(N):
        if floor[j][i] == '|' and l_visited == False:
            l_visited = True
            count += 1
        elif floor[j][i] == '-':
            l_visited = False

print(count)


