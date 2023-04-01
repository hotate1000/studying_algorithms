from enum import Enum;
from list4_3 import FixedQueue;

Menu = Enum('Menu', ['エンキュー', 'デキュー', 'ピーク', '探索', 'ダンプ', '終了']);
# a = [f'({m.value}){m.name}' for m in Menu];
# print(a);

def select_menu() -> Menu:
    s = [f'({m.value}){m.name}' for m in Menu];
    while True:
        print(*s, sep=' ', end='');
        n = int(input(':'));
        if 1 <= n <= len(Menu):
            return Menu(n);

q = FixedQueue();

while True:
    print(f'現在のデータ数：{len(q)} / {q.capacity}');
    menu = select_menu();

    if menu == Menu.エンキュー:
        x = int(input('データ：'));
        try:
            q.enque(x);
        except FixedQueue.Full:
            print('キューが満杯です。');
    elif menu == Menu.デキュー:
        try:
            x = q.deque();
            print(f'デキューしたデータは{x}です。');
        except FixedQueue.Empty:
            print('キューが空です。');
    elif menu == Menu.ピーク:
        try:
            x = q.peek();
            print(f'ピークしたデータは{x}です。');
        except FixedQueue.Empty:
            print('キューが空です');
    elif menu == Menu.探索:
        x = int(input('値：'));
        if x in q:
            print(f'{q.count(x)}個含まれ先頭の位置は{q.find(x)}です。');
        else:
            print('その値は含まれません。');
    elif menu == Menu.ダンプ:
        q.dump();
    else:
        break;
