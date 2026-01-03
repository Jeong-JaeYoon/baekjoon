import math

n = int(input())

for _ in range(n):
    a, b = map(int, input().split())
    result = math.lcm(a,b)
    print(result)

# 다른 답안

# n = int(input())

# for _ in range(n):
#     a, b = map(int, input().split())
#     c = math.gcd(a, b)
#     print((a*b)/c)
