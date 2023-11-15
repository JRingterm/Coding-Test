h, m = map(int, input().split(" "))
cook = int(input())

time = h * 60 + m + cook

newh = time // 60 % 24
newm = time % 60

print(newh, newm)