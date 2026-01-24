from collections import Counter
import sys

n = int(sys.stdin.readline())
card_count = Counter(list(map(int, sys.stdin.readline().split())))

m = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))

for num in num_list:
    print(card_count[num], end=' ')