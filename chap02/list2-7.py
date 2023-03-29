def card_conv1(n: int, x:int) -> str:
    answer ='';
    if x > 10:
        answer = '10進数以下の値を入力ください。';
        return answer;
    while(n // x > 0):
        b = n % x;
        n = n // x;
        answer = str(b) + answer;
    answer = str(n) + answer;
    return answer;

# print(card_conv1(13, 8));
# print(card_conv1(13, 2));

def card_conv2(x: int, r:int) -> str:
    d = '';
    dchar = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ';

    while x > 0:
        d += dchar[x % r];
        x //= r;
    return d[::-1];

if __name__ == '__main__':
    while True:
        while True:
            no = int(input('10進数の値を入力。'));
            if no > 0:
                break;
        while True:
            cd = int(input('何進数に変換するか？(2~36)'));
            if 2 <= cd <= 36:
                break;
        print(f'{cd}変数では{card_conv2(no, cd)}。')
        retry = input("再度行いますか？(Y/N)");
        if retry in {'N', 'n'}:
            break;
