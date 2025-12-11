n = int(input())
num_list = []

for i in range(2, n+1):
    if n == 1:
        break
    while n % i == 0:
        n = n / i
        print(i)
