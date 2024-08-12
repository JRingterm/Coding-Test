import sys

input = sys.stdin.readline

N, K = map(int, input().split())
measure = []

for i in range(1, N+1):
    if N % i == 0:
        measure.append(i)

if len(measure) >= K:
    print(measure[K-1])
else:
    print(0)
