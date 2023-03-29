from typing import Any, MutableSequence, Sequence;

def reverse_array(a: MutableSequence) -> None:
    a_len = len(a);
    a_len_f = a_len // 2;
    for i in range(a_len_f):
        a[i],a[a_len-i-1] = a[a_len-i-1],a[i];

if __name__ == '__main__':
    n = 7;
    x = [None] * n;
    x[0],x[1],x[2],x[3],x[4],x[5],x[6] = 2, 5, 1, 3, 9, 6, 7;

    reverse_array(x);
    print(x);
