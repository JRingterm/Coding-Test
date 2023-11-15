import sys
input = sys.stdin.readline

student = list(map(int, range(1,31)))

for _ in range(28):
    a = int(input())
    student.remove(a)
print(min(student))
print(max(student))


        