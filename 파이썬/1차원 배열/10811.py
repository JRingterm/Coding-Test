import sys
input = sys.stdin.readline

n,m = map(int, input().split())
basket = list(range(1,n+1))

for _ in range(m):
    i, j = map(int, input().split())
    temp = basket[i-1:j]
    temp.reverse()
    basket[i-1:j] = temp
    #또는 temp 대신 쓸 수 있는 방법
    #k = basket[i-1:j]
    #basket = basket[:i-1] + k[::-1] + basket[j:]
print(*basket)