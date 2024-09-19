import sys

input = sys.stdin.readline

T = int(input())

for i in range(T):
    n = int(input())
    dic = {}
    for _ in range(n):
        name, category = map(str, input().strip().split())
        if category in dic:
            #종류가 이미 있으면 해당 종류에 이름만 추가
            dic[category].append(name)
        else:
            #종류가 없다면 value인 이름을 리스트 형식으로 만들어놓기
            dic[category] = [name]
    cnt = 1

    for j in dic:
        # 해당 의상 종류를 입지 않는 경우 포함. +1
        cnt *= (len(dic[j])) + 1

    #알몸인 경우 제외
    print(cnt - 1)

