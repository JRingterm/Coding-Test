import sys
input = sys.stdin.readline

N = int(input())

sum = 1
i = 1
while True:
    if N <= sum:
        print(i)
        break
    sum += 6*i
    i += 1
