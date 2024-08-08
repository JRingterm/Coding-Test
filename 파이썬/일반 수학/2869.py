import sys

input = sys.stdin.readline

A, B, V = map(int,input().split())
day_move = A - B     #하루에 갈 수 있는 거리
total_length = V - B   #정상에 가면 안미끄러지니까, 총 가야할 거리

if total_length % day_move == 0:
    print(total_length // day_move)
else:
    print(total_length // day_move + 1)