# list = [6, 4, 3, 7, 1, 9, 8];
# print(list);

# for k in range(len(list) - 1):
#     for i in range(len(list) - 1):
#         j = len(list) - i - 1;
#         if list[j] < list[j - 1]:
#             list[j],list[j - 1] = list[j - 1],list[j];

# print(list);


from typing import MutableSequence;

def bubble_sort1(a: MutableSequence) -> None:
    n = len(a);
    for i in range(n-1):
        for j in range(n-1, i, -1):
            if a[j-1] > a[j]:
                a[j-1], a[j] = a[j], a[j-1];


def bubble_sort2(a: MutableSequence) -> None:
    n = len(a);
    for i in range(n-1):
        exchng = 0;
        for j in range(n - 1, i, -1):
            if a[j - 1] > a[j]:
                a[j - 1], a[j] = a[j], a[j - 1];
                exchng += 1;
        if exchng == 0:
            break;


def bubble_sort3(a: MutableSequence) -> None:
    n = len(a);
    k = 0;
    while k < n - 1:
        last = n - 1;
        for j in range(n - 1, k, -1):
            if a[j - 1] > a[j]:
                a[j - 1], a[j] = a[j], a[j - 1];
                last = j;
        k = last;

if __name__ == '__main__':
    print('単純交換ソート（バルブソート）');
    x = [6, 4, 3, 7, 1, 9, 8];
    bubble_sort3(x);
    print(x);
