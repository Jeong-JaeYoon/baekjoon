num_list = []

for _ in range(5):
    n = int(input())
    num_list.append(n)

avg = int(sum(num_list)/5)
print(avg)

num_list.sort()
med = num_list[2]
print(med)