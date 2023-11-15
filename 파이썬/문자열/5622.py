alpha = input()
time = 0

#S = 83 -> 9 8이 나와야하는데 9가 나옴.
for i in alpha:
    time += 3+(ord(i)%65)//3
print(time)

