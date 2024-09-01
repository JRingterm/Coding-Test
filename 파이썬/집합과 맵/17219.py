import sys

input = sys.stdin.readline

N, M = map(int, input().split())
f = dict()
result = []

for i in range(N):
    site, pw = map(str, input().split())
    f[site] = pw

for i in range(M):
    site = input().strip()
    print(f[site])