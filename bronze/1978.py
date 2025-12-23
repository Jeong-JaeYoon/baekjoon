n = int(input())
num_list = list(map(int, input().split()))
count = 0

for i in num_list:
    result = True

    if i == 1:
        continue

    for j in range(2, i):
        if i % j == 0:
            result = False

    if result is True:
        count += 1

print(count)