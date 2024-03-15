import sys
input = sys.stdin.readline

n = int(input())
A = []
subtract = 0

for i in range(n):
    A.append((input().strip())) #\n 없애기 위해 .strip()

for word in A:
    alpha = list(word)
    check = []
    for i in range(len(alpha)):
        if i!=0:
            if alpha[i] not in check:
                if i == len(alpha)-1:
                    check.append(alpha[i])
                elif alpha[i-1] == alpha[i]:
                    continue
                check.append(alpha[i-1])
            else:   
                subtract += 1
                break
print(n-subtract)

            


        


        




        
    