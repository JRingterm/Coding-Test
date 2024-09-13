import sys

input = sys.stdin.readline

N, M = map(int, input().split())

trees = list(map(int, input().split()))
trees.sort(reverse = True)

start = 0
end = max(trees)

#이진탐색
while start <= end:
    H = (start+end)//2   #중간값을 절단기의 높이 H로 설정.
    get = 0     #얻을 수 있는 나무길이
    for i in trees:
        if i > H:
            get += i - H
    
    #얻을 수 있는 나무길이와 목표 길이를 비교하면서 절단기의 높이를 낮추거나 높인다.
    if get < M:
        end = H - 1
    else:
        start = H + 1
#절단기에 설정할 수 있는 높이의 최대값이므로, end가 최대값이 된다.
print(end)


