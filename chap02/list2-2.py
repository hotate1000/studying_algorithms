from typing import Any, Sequence;

# 受け取り値がシーケンス型であること、返却は任意の型
def max_of(a: Sequence) -> Any:
    maximum = a[0];
    for i in range(1, len(a)):
        if a[i] > maximum:
            maximum = a[i];
    return maximum;

if __name__ == '__main__':
    num = 5;
    x = [None] * num;
    x[0],x[1],x[2],x[3],x[4] = 172, 153, 192, 140, 165;

    print('最大値：', max_of(x));
