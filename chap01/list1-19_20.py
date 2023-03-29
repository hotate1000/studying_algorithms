for i in range(1, 13):
    if i == 8:
        continue;
    print(i, end=' ');
print();

listA = list(range(1,8));
listB = list(range(9,13));
listC = listA + listB

for i in listC:
    print(i, end=' ');
