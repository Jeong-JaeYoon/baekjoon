n = int(input())
num_list = []

for _ in range(n):
    a, b = map(int, input().split())
    num_list.append((b,a))

num_list.sort()

for b, a in num_list:
    print(a, b)