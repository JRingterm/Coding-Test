import sys
input = sys.stdin.readline

word_list = []
result = ""

for i in range(5):
    word_list.append(input().strip())

max_len = max(len(word) for word in word_list)

for i in range(max_len):
    for j in range(5):
        if i < len(word_list[j]):
            result += word_list[j][i]
print(result)