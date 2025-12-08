res_dict = {}

for _ in range(5):
    word = str(input())
    for i, n in enumerate(word):
        if f'{i}' not in res_dict.keys():
            res_dict[f'{i}'] = n
        else:
            res_dict[f'{i}'] = res_dict[f'{i}'] + n

print(''.join(res_dict.values()))
