from itertools import permutations

n = int(input())
result = list(permutations(range(n), 2))

print(len(result))