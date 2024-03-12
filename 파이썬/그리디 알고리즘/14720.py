import sys
input = sys.stdin.readline

n = int(input())
count = 0
store = list(map(int, input().split()))

current = 0 #처음은 딸기우유

for i in store:
    #다음 가게가 (최근마신우유 + 1) % 3에 해당하는 가게라면 카운트+1
    if current == i:
        count += 1
        current = (current + 1) % 3
    else:
        continue

print(count)
