start = int(input())
end = int(input())

num_list = []

for i in range(start, end+1):
    flag = True
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                flag = False
                break
        if flag:
            num_list.append(i)

if len(num_list) == 0:
    print(-1)
else:
    print(sum(num_list))
    print(num_list[0])