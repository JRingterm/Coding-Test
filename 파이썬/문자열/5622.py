import sys
input = sys.stdin.readline

alpha_list = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
time = 0

word = input()

for i in word:
    for idx, alpha in enumerate(alpha_list):
        if i in alpha:
            time += idx+3
print(time)
