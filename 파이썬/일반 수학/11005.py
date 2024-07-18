import sys
input = sys.stdin.readline

N, B = map(int, input().split())

num = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
result = ""

while N != 0:
    result += num[N % B]
    N = N//B

result = ''.join(reversed(result))

print(result)

