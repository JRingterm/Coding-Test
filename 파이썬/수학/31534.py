import sys
import math
input = sys.stdin.readline

a, b, h = map(int, input().split())
if a==0:
    t = math.sqrt(h**2 + b**2)
    donut = t**2 * math.pi
    print(donut)
elif a==b:
    print(-1)
else:
    if a>b:
        a, b = b, a
    H = -b*h / (a-b)
    big_radius = math.sqrt(H**2 + b**2)
    small_radius = big_radius*a/b

    big_circle = big_radius**2 * math.pi
    small_circle = small_radius**2 * math.pi

    donut = big_circle - small_circle
    print(donut)