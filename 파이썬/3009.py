import math as m

x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

def line(x1, y1, x2, y2):
    line = m.sqrt((x1-x2)**2) + m.sqrt((y1-y2)**2)
    return line


