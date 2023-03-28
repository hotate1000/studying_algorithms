n = 14;
w = 5;

# for i in range(n):
#     print('*', end='');
#     if i % w == w - 1:
#         print();
# if n % w:
#     print();

for _ in range(n // w):
    print('*' * w);
if n % w != 0:
    print('*' * (n % w));
