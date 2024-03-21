import sys
input = sys.stdin.readline

N = int(input())
member = [[0] * 2 for _ in range(N)]

for i in range(N):
    age, name = input().split()
    member[i][0]=(int(age))
    member[i][1]=(name)
member.sort(key=lambda x:x[0])

for i in range(N):
    print(member[i][0], member[i][1])