n = int(input())
candies = list(map(int, input().split()))
even = []
odd = []

for candy in candies:
    if candy % 2 == 0:
        even.append(candy)
    else:
        odd.append(candy)

result = sum(even)
odd.sort(reverse=True)

if len(odd) % 2 == 0:
    result += sum(odd)
else:
    result += sum(odd[:-1])
    
print(result)