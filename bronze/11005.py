num_list = '''0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'''
answer = ''

n, b = map(int, input().split())

while n!=0:
    answer = num_list[n % b] + answer
    n //= b

print(answer)
