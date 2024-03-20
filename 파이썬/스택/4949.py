import sys
#input = sys.stdin.readline

while True:
    s = input()
    stack = []
    flag = True

    if s == ".":
        break
    for i in s:
        if i=="(" or i=="[":
            stack.append(i)
        elif i==")":
            if len(stack) == 0 or stack[-1] != "(":
                flag = False
                break
            stack.pop()
        elif i=="]":
            if len(stack) == 0 or stack[-1] != "[":
                flag = False
                break
            stack.pop()
    if flag == False:
        print("no")
    elif len(stack) == 0:
        print("yes")
    else:
        print("no") #이 조건을 추가 안해줘서 "(" 만 있는 입력을 처리 못함.