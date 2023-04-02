def factorial(n: int) -> int:
    if n > 0:
        return n * factorial(n - 1);
    else:
        return 1;

if __name__ == '__main__':
    n = int(input('何の階乗か？'));
    print(f'{n}の階乗は{factorial(n)}です');
