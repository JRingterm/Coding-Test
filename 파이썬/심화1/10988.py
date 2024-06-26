import sys
input = sys.stdin.readline

word = input().strip() #문자열 입력은 개행문자가 포함되기 때문에 제거해야한다.
flag = True

for i in range(0, len(word)//2):
    flag = True
    if word[i] != word[-(i+1)]:
        flag = False
        break
        
if flag == True:
    print(1)
else:
    print(0)