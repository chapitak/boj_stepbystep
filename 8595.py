test_num = int(input())
input_ox = []
sum_list = []
for _ in range(test_num):
    input_ox.append(input())
for i in range(test_num):
    point_per_question = 0
    sum_per_case = 0
    for j in range(len(input_ox[i])):
        if input_ox[i][j] == 'O':
            point_per_question += 1
        else:
            point_per_question = 0
        sum_per_case += point_per_question
    sum_list.append(sum_per_case)
print(*sum_list, sep="\n")

