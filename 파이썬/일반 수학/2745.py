import sys
input = sys.stdin.readline

N, B = input().split()
N = ''.join(reversed(N)) #문자열 뒤집기
B = int(B)

num = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ" #알파벳으로 표시되는 진법을 숫자로 바꾸기 위한 문자배열

result = 0

for i in range(0, len(N)):
    result += B**i * num.index(N[i])  #진법 계산식

print(result)