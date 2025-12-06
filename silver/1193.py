n = int(input())
line = 1

while n > line:
    n -= line
    line += 1

if line % 2 == 0:
    print(f'{1 + (n - 1)}/{line - (n - 1)}')
else:
    print(f'{line - (n - 1)}/{1 + (n - 1)}')