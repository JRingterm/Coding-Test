list1 = list(map(int, input().split(" ")))
list2 = [1,1,2,2,2,8]
list3 = [list2[i] - list1[i] for i in range(len(list1))]

for i in range(len(list3)):
    if list3[i] > 0:
        list3[i] + list3[i]
    elif list3[i] < 0:
        list3[i] - list3[i]
    else:
        continue

print(*list3)