while True:
    n = int(input())
    if n == -1:
        break

    num_list = []

    for i in range(1, n+1):
        if n % i == 0:
            num_list.append(i)

    if sum(num_list[:-1]) == n:
        result = " + ".join(map(str, num_list[:-1]))
        print(f'{n} = {result}')
    else:
        print(f'{n} is NOT perfect.')
