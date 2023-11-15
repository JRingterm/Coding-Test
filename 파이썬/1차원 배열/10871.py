n, x = map(int, input().split())
a = list(map(int,input().split())) #리스트는 map 쓰기

for i in a:
    if i < x:
        print(i, end=' ')
