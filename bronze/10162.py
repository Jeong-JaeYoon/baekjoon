n = int(input())

if n % 10 != 0:
    print(-1)
    
else:
    a, b = divmod(n, 300)
    print(a, end=' ')
    c, d = divmod(b, 60)
    print(c, end=' ')
    print(int(d/10))