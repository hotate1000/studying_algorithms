from typing import Any, Sequence;
import copy;


def seq_search(seq: Sequence, key: Any) -> int:
    a = copy.deepcopy(seq);
    # 答えを追加し、範囲を検索するif文を減らしている
    a.append(key);
    i = 0;
    while True:
        if a[i] == key:
            break;
        i += 1;
    return -1 if i == len(seq) else i;

if __name__ == '__main__':
    seq = [6,4,3,2,1,2,8];
    key = 2;
    answer = seq_search(seq, key);
    if answer == -1:
        print('その要素は存在しません');
    else:
        print(f'それはx[{answer}]にあります。');
