n = int(input())
count = 0

while True:
    if n >= 5:
        n -= 5
        count += 1
    elif 3 <= n < 5:
        n -= 3
        count += 1
    else:
        break

if n == 0:
    print(count)
else:
    print(-1)