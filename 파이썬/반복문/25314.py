import sys
input = sys.stdin.readline()

n = int(input)

for i in range(n//4):
    print("long ", end='')
print("int")

#모범 답안
#print(int(input())//4*'long '+'int')