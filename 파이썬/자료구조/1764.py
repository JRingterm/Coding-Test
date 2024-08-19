import sys

input = sys.stdin.readline

N, M = map(int, input().split())
names = dict()
result = []

for i in range(N):
    name = input().strip()
    names[name] = i

for i in range(M):
    Q_input = input().strip()
    if Q_input in names:
        result.append(Q_input)

result.sort()
print(len(result))
for i in result:
    print(i)
