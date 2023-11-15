pay = int(input())
n = int(input())
c = 0
for i in range(n):
    a, b = map(int, input().split())
    c = c + a * b

if c == pay:
    print("Yes")
else:
    print("No")
