from typing import Sequence, Any;

def bin_search(list: Sequence, key: int) -> int:
    pl = 0;
    pr = len(list) - 1;
    while True:
        pc = (pl + pr) // 2;
        if list[pc] == key:
            return pc;
        elif list[pc] < key:
            pl = pc + 1;
        else:
            pr = pc - 1;
        if pl > pr:
            break;
    return -1;

if __name__ == "__main__":
    list = [5, 7, 15, 28, 29, 31, 39, 58, 68, 70, 95];
    key = 1;
    id = bin_search(list, key);
