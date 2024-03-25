import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = set()
count = 0

for _ in range(N):
    A.add(input().strip())

for _ in range(M):
    check = input().strip()
    if check in A:
        count += 1

print(count)