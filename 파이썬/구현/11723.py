#구현, 비트마스킹
import sys

sys.stdin = open("C:\\Users\\hojun\\Desktop\\input.txt", "r")
input = sys.stdin.readline

M = int(input())
S = set()

for i in range(M):
    # all, empty는 입력이 한 개라서, 다른 명령들과 구분할 필요가 있다.
    Q_input = input()
    inputs = list(map(str, Q_input.split()))  #우선 리스트에 명령, 숫자 를 입력받는다

    command = inputs[0]     #일단 명령은 다 있으니까 바로 입력
    if len(inputs) == 2:    #all, empty는 입력이 하나이므로 나머지 명령에 대해서는 n까지 추가
        n = int(inputs[1])
    
    if command == "add":
        S.add(n)
    elif command == "remove":
        S.discard(n)   #discard()는 삭제할 요소가 집합에 존재하지 않는 경우 KeyError 발생x
    elif command == "check":
        if n in S:
            print(1)
        else:
            print(0)
    elif command == "toggle":
        if n in S:
            S.remove(n)
        else:
            S.add(n)
    elif command == "all":
        S = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20}
    elif command == "empty":
        S.clear()

