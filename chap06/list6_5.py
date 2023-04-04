from typing import MutableSequence;

def shaker_sort(a: MutableSequence) -> None:
    left = 0;
    right = len(a) - 1;
    last = right;
    while left < right:
        for j in range(right, left, -1):
            if a[j - 1] > a[j]:
                a[j - 1], a[j] = a[j], a[j - 1];
                last = j;
            left = last;
        for j in range(left, right, 1):
            if a[j] > a[j + 1]:
                a[j + 1], a[j] = a[j], a[j + 1];
                last = j;
            right = last;

if __name__ == '__main__':
    x1 = [6, 4, 3, 7, 1, 9, 8];
    x2 = [9, 1, 3, 4, 6, 7, 8];
    shaker_sort(x1);
    print(x1);
    shaker_sort(x2);
    print(x2);
