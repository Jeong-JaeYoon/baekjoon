n = int(input())

for i in range(1, n+1):
    num_split = [int(j) for j in str(i)]
    sum_result = i + sum(num_split)
    if sum_result == n:
        break

if i == n:
    print(0)
else:
    print(i)