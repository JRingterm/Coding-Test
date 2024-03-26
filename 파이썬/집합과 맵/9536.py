import sys
input = sys.stdin.readline

T = int(input())
crying = set()

for i in range(T):
    S = input().strip().split()

    while True:
        c = input().strip()
        if c == "what does the fox say?":
            break
        crying.add(c.split()[2])

    S = [i for i in S if i not in crying]

    for i in range(len(S)):
        print(S[i], end=' ')