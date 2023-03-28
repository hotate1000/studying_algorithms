n = 13;
answer = '';

for _ in range(n//2):
    answer += '+-';
if n % 2 == 1:
    answer += '+';

print(answer);
