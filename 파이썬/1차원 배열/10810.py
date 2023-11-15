import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = []
for _ in range(n):
    a.append(0)
#위 for문 아래 코드가 시간복잡도상 더 좋음.
# a = [0] * n
for _ in range(m):
    i, j, k = map(int, input().split())
    for c in range(i-1,j):
        a[c] = k


print(*a)