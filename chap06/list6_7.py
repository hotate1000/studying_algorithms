from typing import MutableSequence;

def insertion_sort(a: MutableSequence) -> None:
    n = len(a);
    for i in range(1, n):
        j = i;
        tmp = a[i];
        while j > 0 and a[j - 1] > tmp:
            a[j] = a[j -1];
            j -= 1;
        a[j] = tmp;

if __name__ == '__main__':
    x1 = [6, 4, 3, 7, 1, 9, 8];
    x2 = [9, 1, 3, 4, 6, 7, 8];
    insertion_sort(x1);
    print(x1);
    # insertion_sort(x2);
    # print(x2);
    