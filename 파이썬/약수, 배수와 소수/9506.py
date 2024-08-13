import sys
input = sys.stdin.readline

while True:
    n = int(input())
    measure = []
    if n == -1:  #-1이면 입력종료
        break

    sum = 0
    for i in range(1, n-1): #약수 구하기
        if n % i == 0:
            measure.append(i)
            sum += i

    result_str = ""
    if n == sum: #n이 완전수이면
        for i in range(len(measure)):
            if measure[i] == measure[-1]:
                result_str += str(measure[i])
            else:
                result_str += str(measure[i]) + " + "
        print(f'{n} = {result_str}')
    else:   #n이 완전수가 아니면
        print(f'{n} is NOT perfect.')
