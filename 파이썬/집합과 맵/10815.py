import sys
input = sys.stdin.readline

N = int(input())
S_card= set(input().split())

M = int(input())
check = input().split()

# result = []
for i in check:
    if i in S_card:
        print(1, end=' ')
    else:
        print(0, end=' ')

# for i in result:
#     print(i, end=' ')



