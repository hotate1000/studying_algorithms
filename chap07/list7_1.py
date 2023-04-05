def bf_match(txt: str, pat: str) -> int:
    pt = 0;
    pp = 0;

    while pt != len(txt) and pp != len(pat):
        if txt[pt] == pat[pp]:
            pt += 1;
            pp += 1;
        else:
            pt = pt - pp + 1;
            pp = 0;

    return pt - pp if pp == len(pat) else - 1;

if __name__ == '__main__':
    s1 = 'ABCDEFGHI';
    s2 = 'DE';
    idx = bf_match(s1, s2);

    if idx == -1:
        print('テキストの中にパターンは存在しません。');
    else:
        print(f'{(idx + 1)}文字目にマッチします。');
