num_list = list(map(int, input().split()))
num_list.sort()

a, b, c = num_list

if c >= a + b:
    print(2*(a+b)-1)
else:
    print(a+b+c)