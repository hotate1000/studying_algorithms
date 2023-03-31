from enum import Enum;
from list4_1 import FixedStack;

Menu = Enum('Menu', ['プッシュ', 'ホップ', 'ピーク', '探索', 'ダンプ', '終了']);

def select_menu() -> Menu:
    s = [f'({m.value}){m.name}' for m in Menu];
    while True:
        print(*s, sep=' ', end='');
        n = int(input(' : ')) + 1;
        if 1 <= n <= len(Menu):
            return Menu;

s = FixedStack(64);

while True:
    print(f'現在のデータ数：{len(s)}/{s.capacity}');
    menu = select_menu();

    if menu == Menu.プッシュ:
        x = int(input('データ：'));
        try:
            s.push(x);
        except FixedStack.Full:
            print('スタックが満杯です。');
    elif menu == Menu.ホップ:
        try:
            x = s.pop();
            print(f'ホップしたデータは{x}です。');
        except FixedStack.Empty:
            print('スタックが空です。');
    elif menu == Menu.ピーク:
        try:
            x = s.peek();
            print(f'ピークしたデータは{x}です。');
        except FixedStack.Empty:
            print('スタックが空です。');
    elif menu == Menu.探索:
        x = int(input('値：'));
        if x in s:
            print(f'{s.count(x)}こ含まれ先頭の位置は{s.find(x)}です。');
        else:
            print('その値は含ませません');
    elif menu == Menu.ダンプ:
        s.dump();
    else:
        break;