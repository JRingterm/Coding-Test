import sys
input = sys.stdin.readline

dic = {"A+":4.5, "A0":4.0, "B+":3.5, "B0":3.0, "C+":2.5, "C0":2.0, "D+":1.5, "D0":1.0, "F":0.0}
sub_score = 0
mult = 0

for i in range(20):
    subject, score, grade = input().split()
    if grade != "P":
        sub_score += float(score)
        mult += float(score) * dic[grade]

print(mult / sub_score)