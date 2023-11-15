h, m = map(int, input().split(" "))

alarm = h * 60 + m - 45

newh = alarm // 60 % 24
newm = alarm % 60

print(newh, newm)