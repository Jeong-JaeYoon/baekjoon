import sys

input = sys.stdin.readline
n = int(input())
record = []

for _ in range(n):
    num = int(input())
    if num == 0:
        record.pop()
    else:
        record.append(num)

print(sum(record))