from itertools import combinations

n, m = map(int, input().split())
num_list = list(map(int, input().split()))
answer = 0

combi_result = list(combinations(num_list, 3))

for i in combi_result:
    sum_result = sum(i)
    if (sum_result <= m) and (sum_result > answer):
        answer = sum_result

print(answer)