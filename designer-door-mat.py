N, M = map(int, input().split())
dotbar = 1
lines = int((M - 3) / 2)
# For the first lines before the 'WELCOME'
for c in range(int((N-1) / 2)):
    print('-' * lines, end='')
    print('.|.' * dotbar, end='')
    print('-' * lines)
    dotbar += 2
    lines -= 3
# For the 'WELCOME' part
print('-' * int((M-7) / 2), end='')
print('WELCOME', end='')
print('-' * int((M-7) / 2))
# For the lines after the 'WELCOME'
dotbar = int((((N - 1) / 2) * 2) - 1)
lines = 3
for c in range(int((N-1) / 2)):
    print('-' * lines, end='')
    print('.|.' * dotbar, end='')
    print('-' * lines)
    lines += 3
    dotbar -= 2

