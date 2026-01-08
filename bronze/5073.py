while True:
    num_list = list(map(int, input().split()))
    num_list = sorted(num_list)

    if sum(num_list) == 0:
        break

    a, b, c = num_list

    if c >= a + b:
        print('Invalid')
    else:
        first = a == b
        second = b == c
        third = c == a
        condition = first + second + third

        if condition == 3:
            print('Equilateral')
        elif condition == 1:
            print('Isosceles')
        else:
            print('Scalene')