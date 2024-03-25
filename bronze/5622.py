dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

inp = input()
ans = 0

for j in range(len(inp)):
    for i in dial:
        if inp[j] in i:
            ans += dial.index(i)+3

print(ans)
