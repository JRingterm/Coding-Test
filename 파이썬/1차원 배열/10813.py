import sys
input = sys.stdin.readline

n, m = map(int, input().split())
basket = []

for i in range(n):
    basket.append(i+1)
#위 코드는 아래 코드로 대체
#basket = list(range(1,n+1))

for _ in range(m):
    a,b = map(int, input().split())
    temp = basket[a-1]
    basket[a-1] = basket[b-1]
    basket[b-1] = temp

print(*basket)
    