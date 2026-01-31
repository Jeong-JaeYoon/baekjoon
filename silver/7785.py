import sys

n = int(sys.stdin.readline())
record = dict()

for _ in range(n):
    name, status = map(str, sys.stdin.readline().split())

    if status == 'enter':
        record[name] = status
    
    else:
        del record[name]

record = sorted(record.keys(), reverse=True)

for name in record:
    print(name)
