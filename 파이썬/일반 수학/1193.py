import sys

input = sys.stdin.readline

X = int(input())

line = 1

while X > line: #몇 번째 줄에 해당하는지 체크
    X -= line
    line += 1

if line % 2 == 0:
    numer = X
    denom = line-(X-1)
else:
    numer = line-(X-1)
    denom = X

print(f'{numer}/{denom}')