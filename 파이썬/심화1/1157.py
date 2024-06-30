import sys
input = sys.stdin.readline

word = input().strip().upper()
alpha = list(set(word))

cnt = []

for i in alpha:
    c = word.count(i)
    cnt.append(c)

if cnt.count(max(cnt)) > 1:
    print("?")
else:
    print(alpha[(cnt.index(max(cnt)))])
