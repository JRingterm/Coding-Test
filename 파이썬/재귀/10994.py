import sys
input = sys.stdin.readline

N = int(input())
length = 4*N-3
star_array = [[' ']*(length) for _ in range(length)]

def star(n,x,y):
    global star_array

    length = 4*n-3
    if length == 1:
        star_array[x][y] = '*'
        return
    for i in range(length):
        star_array[x][y+i] = '*'
        star_array[x+i][y] = '*'
        star_array[x+(length-1)][y+i] = '*'
        star_array[x+i][y+(length-1)] = '*'
    n -= 1
    x += 2
    y += 2
    star(n,x,y)
    return

star(N,0,0)
for i in range(length):
    print(*star_array[i], sep='')


        