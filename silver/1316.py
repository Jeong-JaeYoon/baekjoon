result = int(input())

for _ in range(result):
    temp = []
    for s in input():
        if s not in temp:
            temp.append(s)
        else:
            if temp[-1] != s:
                result -= 1
                break
            
print(result)