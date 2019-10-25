input_list = []
unique_count = 0
for i in range(10):
    input_list.append(int(input())%42)
# print(input_list)
for i in input_list:
    overlap_size = input_list.count(i)
    if overlap_size != 1:
        unique_count += 1/overlap_size
    else: 
        unique_count += 1
print(int(unique_count))



#count를 한다면? 