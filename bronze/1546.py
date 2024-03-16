n = int(input())
scores = list(map(int, input().split()))

m = max(scores)

total = 0

for i in range(n):
    total += (scores[i]/m)*100

print(total/n)