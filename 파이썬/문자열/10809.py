s = input()
alpha = [-1] * 26
for i in range(len(s)):
    if alpha[ord(s[i]) - 97] == -1:
        alpha[ord(s[i]) - 97] = i

print(*alpha)

#s = input()
#for i in range(97,123):
#    print(s.find(chr(i)), end=' ')
#find()는 문자열에서 그 문자가 등장하는 첫 인덱스를 반환한다.