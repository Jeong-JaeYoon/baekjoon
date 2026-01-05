n, m = map(int, input().split())
a = []
b = []
answer = []

for i in range(2*n):
    if i < n:
        a.append(list(map(int, input().split())))
    else:
        b.append(list(map(int, input().split())))
        
for i in range(n):
    temp = []
    for j in range(m):
        temp.append(str(a[i][j]+b[i][j]))
    answer.append(temp)
    
for row in answer:
    print(' '.join(row))