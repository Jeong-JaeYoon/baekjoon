n = 20
num_list, grade_list = [], []
grade_map = {'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0, 'C+': 2.5, 'C0': 2.0, 'D+': 1.5, 'D0': 1.0, 'F': 0.0}
num_sum = 0
grade_sum = 0

for _ in range(n):
    _, num, grade = input().split()
    num_list.append(num)
    grade_list.append(grade)

num_list = list(map(float, num_list))

for i in range(n):
    if grade_list[i] == "P":
        continue
    else:
        grade_sum += grade_map[grade_list[i]] * num_list[i]
        num_sum += num_list[i]
        
print(grade_sum/num_sum)