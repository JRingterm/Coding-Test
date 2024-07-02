import sys
input = sys.stdin.readline

word = input().strip()
croatia = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

for i in croatia:
    word = word.replace(i, "*")
print(len(word))