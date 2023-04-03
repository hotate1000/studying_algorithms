def recur(n: int) -> int:
    # if n > 0:
    #     recur(n - 1);
    #     print(n);
    #     recur(n - 2);
    while n > 0:
        recur(n - 1);
        print(n);
        n = n - 2;

x = int(input('整数を入力：'));
recur(x);
