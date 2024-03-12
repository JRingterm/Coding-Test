import sys
input = sys.stdin.readline

n, k = map(int, input().split())
A = []
count = 0

for i in range(n):
    A.append(int(input()))
A.reverse()

for i in A:
    remain = k % i
    if remain == k:
        continue
    count += k // i
    k = remain

print(count)