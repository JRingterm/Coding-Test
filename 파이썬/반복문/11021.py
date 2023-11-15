import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
    A,B = map(int, input().split())
    print("Case #", i+1, ": ", A+B, sep='')
    #sep은 단어간 간격을 의미