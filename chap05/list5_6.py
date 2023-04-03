def move(no: int, x: int, y: int) -> None:
    if no > 1:
        move(no-1, x, 6-x-y);
    print(f'円盤[{no}]を{x}軸から{y}軸へ');
    if no > 1:
        move(no-1, 6-x-y, y);

n = int(input('ハノイの塔：円盤の枚数：'));
move(n, 1, 3);
