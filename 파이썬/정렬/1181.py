import sys
input = sys.stdin.readline

N = int(input())
word_list = []

for _ in range(N):
    word_list.append(input().strip())

word_list = list(set(word_list))  
word_list.sort()
word_list.sort(key=len)

print(*word_list, sep='\n')