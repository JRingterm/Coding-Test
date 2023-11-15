n = int(input())
score = list(map(int, input().split()))

max_score = max(score)
for i in range(n):
    score[i] = score[i]/max_score*100

#위의 for문은 아래로 대체 가능
#print(sum(score)/max(score)*100/n)
print(sum(score)/n)

