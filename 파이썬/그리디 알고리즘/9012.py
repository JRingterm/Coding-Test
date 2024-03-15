import sys
input = sys.stdin.readline

T = int(input())
test_data = []

for i in range(T):
    test_data.append(input().strip())

for i in test_data:
    data_list = list(i)
    stack = []
    flag = True
    for j in data_list:
        if j == "(":
            stack.append(j)
        elif j == ")":
            if len(stack) == 0:
                print("NO")
                flag = False
                break
            stack.pop()
    if flag == False:
        continue
    elif len(stack) == 0:
        print("YES")
        continue
    print("NO")
    


    
