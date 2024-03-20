import sys
input = sys.stdin.readline

K = int(input().strip())
stack = []

for _ in range(K):
    s = int(input().strip())
    if s != 0:
        stack.append(s)
        continue
    stack.pop()

print(sum(stack))
