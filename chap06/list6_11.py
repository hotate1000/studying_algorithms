from typing import MutableSequence;

def qsort(a: MutableSequence) -> None:
    n = len(a);
    pl = 0;
    pr = n - 1;
    x = a[n // 2];

    while pl < pr:
        while a[pl] < x:
            pl += 1;
        while a[pr] > x:
            pr -= 1;
        if pl <= pr:
            a[pl], a[pr] = a[pr], a[pl];
            pl += 1;
            pr -= 1;
    print(f'軸の値は{x}です。');
    print('軸以下のグループ');
    print(*a[0 : pl]);

    if pl > pr + 1:
        print('軸と一致するグループ');
        print(*a[pr + 1 : pl]);

    print('軸以上のグループ');
    print(*a[pr + 1 : n]);


if __name__ == '__main__':
    x1 = [1, 8, 7, 4, 5, 2, 6, 3, 9];
    x2 = [9, 1, 3, 4, 6, 7, 8];
    qsort(x1);
    print(x1);
