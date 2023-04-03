def gcd(x: int, y: int) -> int:
    if y == 0:
        return x;
    else:
        return gcd(y, x % y);

if __name__ == "__main__":
    print('二つの整数の最大公約数を求めます。');
    x = int(input('整数：'));
    y = int(input('整数：'));

    print(F'二つの最大公約数は{gcd(x, y)}です。');
