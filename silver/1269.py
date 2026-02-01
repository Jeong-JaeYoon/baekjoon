import sys

n, m = map(int, sys.stdin.readline().strip().split())
set1 = set(map(int, sys.stdin.readline().strip().split()))
set2 = set(map(int, sys.stdin.readline().strip().split()))

result = set1 ^ set2
print(len(result))
