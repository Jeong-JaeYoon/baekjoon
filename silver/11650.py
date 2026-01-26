n = int(input())
num_list = []

for _ in range(n):
    a, b = map(int, input().split())
    num_list.append((a,b))

num_list.sort()

for a, b in num_list:
    print(f'{a} {b}')