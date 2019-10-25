input_str = input()
input_str_upper = input_str.upper()
input_str_set = list(set(input_str_upper))
count_list = []
for i in input_str_set:
    count_list.append(input_str_upper.count(i))
if count_list.count(max(count_list)) > 1:
    print('?')
else:
    most_frequent = input_str_set[(count_list.index(max(count_list)))]
    print(most_frequent)
