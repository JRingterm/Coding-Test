a = []
for i in range(9):
    a.append(int(input()))
#위 코드를 아래 한줄로 표현 가능
#a = [int(input()) for i in range(9)]

print(max(a))
print(a.index(max(a)) + 1)