n = int(input())
data = [int(input()) for _ in range(n)]

for x in data:
    a, b = divmod(x, 25)
    print(a, end=' ')
    c, d = divmod(b, 10)
    print(c, end=' ')
    e, f = divmod(d, 5)
    print(e, end=' ')
    print(f)