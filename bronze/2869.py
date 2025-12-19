import math

a, b, v = map(int, input().split())

res_len = v - a
climb_len = a - b
day = math.ceil(res_len / climb_len)

print(day+1)