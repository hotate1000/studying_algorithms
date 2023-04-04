from typing import MutableSequence;

def selection_sort(a: MutableSequence) -> None:
    n = len(a);
    for i in range(n - 1):
        min = i;
        for j in range(i + 1, n):
            if a[j] < a[min]:
                min = j;
        a[i], a[min] = a[min], a[i];

if __name__ == '__main__':
    x1 = [6, 4, 3, 7, 1, 9, 8];
    x2 = [9, 1, 3, 4, 6, 7, 8];
    selection_sort(x1);
    print(x1);
    selection_sort(x2);
    print(x2);
