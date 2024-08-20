import sys

input = sys.stdin.readline

N = int(input())
P = list(map(int, input().split()))

P.sort()
result = 0
prev = 0

for i in P:
    prev += i
    result += prev
print(result)



