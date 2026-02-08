from collections import deque

n, k = map(int, input().split())
queue = deque([i+1 for i in range(n)])
result = []

while len(queue) > 0:
    for i in range(k):
        queue.append(queue.popleft())
    result.append(str(queue.pop()))


print('<' + (', ').join(result) + '>')
    