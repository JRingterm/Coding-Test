import sys
input = sys.stdin.readline

N = int(input())
area = [[0 for j in range(100)] for i in range(100)]

for i in range(N):
    x, y = map(int, input().split())
    for X in range(x, x+10):
        for Y in range(y, y+10):
            if area[X][Y] == 0:
                area[X][Y] = 1

count = sum(element == 1 for row in area for element in row)

print(count)