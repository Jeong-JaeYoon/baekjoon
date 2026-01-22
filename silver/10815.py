import sys

n = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))
dic = {cards[i]: 1 for i in range(len(cards))}

m = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

for num in nums:
    print(dic.get(num, 0), end=' ')