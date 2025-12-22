inp = int(input())

output = 1000 - inp
result = 0

def rest_calc(output, coin):
    a, b = divmod(output, coin)
    return a, b

coins = [500, 100, 50, 10, 5, 1]

for coin in coins:
    a, b = rest_calc(output, coin)
    result += a
    output = b

print(result)