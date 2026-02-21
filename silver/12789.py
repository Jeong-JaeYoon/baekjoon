n = int(input())
num_list = list(map(int, input().split()))

stack = []
idx = 1

for num in num_list:
    stack.append(num)

    while stack and stack[-1] == idx:
        stack.pop()
        idx += 1

if stack:
    print('Sad')
else:
    print('Nice')