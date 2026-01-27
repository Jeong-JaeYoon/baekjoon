from collections import deque
import sys

input = sys.stdin.readline

n = int(input().strip())
queue = deque()

for _ in range(n):
    command = str(input().strip())

    if command[0] == '1':
        _, num = command.split()
        queue.appendleft(int(num))

    elif command[0] == '2':
        _, num = command.split()
        queue.append(int(num))

    elif command == '3':
        if queue:
            num = queue.popleft()
            print(num)
        else:
            print(-1)

    elif command == '4':
        if queue:
            num = queue.pop()
            print(num)
        else:
            print(-1)

    elif command == '5':
        print(len(queue))

    elif command == '6':
        if queue:
            print(0)
        else:
            print(1)

    elif command == '7':
        if queue:
            print(queue[0])
        else:
            print(-1)

    elif command == '8':
        if queue:
            print(queue[-1])
        else:
            print(-1)