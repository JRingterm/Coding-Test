import sys

input = sys.stdin.readline

N = int(input())

data = list(map(int, input().split()))
count = 0

for i in data:
    if i == 1:
        continue
    else:
        c = 0
        for j in range(1,i+1):
            if i % j == 0:
                c += 1
        if c == 2:
            count += 1

print(count)