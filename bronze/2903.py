n = int(input())

num = 2

for i in range(1, n+1):
    num += 2**(i-1)

print(num**2)
