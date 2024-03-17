s_count = {chr(i):-1 for i in range(97,123)}

s = list(str(input()))

for i, a in enumerate(s):
    if s_count[a] == -1:
        s_count[a] = i
    else:
        continue

print(*s_count.values())