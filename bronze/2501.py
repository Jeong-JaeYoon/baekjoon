n, k = map(int, input().split())
num_list = []

for i in range(1, n+1):
    a, b = divmod(n, i)
    if b == 0:
        num_list.append(a)

if num_list.__len__() >= k:
    print(num_list[::-1][k-1])
else:
    print(0)
