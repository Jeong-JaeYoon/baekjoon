n = int(input())
limit_list = [1]
count = 1

while True:
    if n <= limit_list[-1]:
        break
    new_limit = limit_list[-1] + 6*count
    limit_list.append(new_limit)
    count += 1

print(len(limit_list))

