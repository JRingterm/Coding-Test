import sys
input = sys.stdin.readline

def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return (fib(n-1) + fib(n-2))

def fibonacci(n):
    f = [0 for _ in range(40)]
    count = 0
    f[0] = 1
    f[1] = 1
    for i in range(2,n):
        f[i] = f[i-1] + f[i-2]
        count += 1
    return count, f[n-1]

n = int(input())
count, answer = fibonacci(n)

print(str(answer) + " " + str(count))

